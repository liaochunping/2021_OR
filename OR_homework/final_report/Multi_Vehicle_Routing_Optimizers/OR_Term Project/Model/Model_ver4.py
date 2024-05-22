# -*- coding: utf-8 -*-
"""
Created on Sat Jan 08 12:02:01 2022

@author: paddy liao
"""
from gurobipy import*
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

def main():
        vehicle= ['car','bike']
        dij = ReadXlsx('Distance Matrix.xlsx',1)
        qi =  ReadXlsx('Virtual Demand.xlsx',2)
        coordinate = ReadXlsx('Coordinate.xlsx',3)
        for _ in range(2):              
                print('delivery by '+'{}'.format(vehicle[_]))
                m = Model('Final_project_test')
                #m.setParam('TimeLimit', 10)
                m.setParam('OutputFlag', False)
                ###################################
                #interger parameters
                Pk =[500,200]                         #capacity of vehicle k
                Ck =[0.0035,0.00025]                      #cost of vehicle k per unit distance
                Vk =[20,15]                           #velocity of a vehcle k
                Dij =dij                                #distance between any pair of node i,j 
                P = 120                                 #price of a burger
                Qi = qi                                 #burger demand of a node
                T = 20/60                                 #maximum total travel time 
                L = len(Dij)                            #Max number of cities a salesman can visit
                K = 0                                   #Minimum number of cities a salesman can visit
                me = 2                                  #Number of salesmen            
                m.update()
                ###################################
                #Binary variables
                n =len(Dij)             #number of nodes
                X ={}                   #initialize the varibales whether goes from node i to j     
                uX={}                   #subtour elimation variables for MTZ method
                pa=1                    #to be the maximum number of nodes that can be visited by any salesman
                for i in range(n):
                    uX[i]=m.addVar(vtype = 'I',name='u'+str(i)) #subtour elimation
                    for j in range(n):
                       X[i,j] = m.addVar(vtype ='B' , name='e_'+str(i)+'_'+str(j))
                m.update()     
                ####################################
                #Obiective
                m.setObjective(quicksum(X[i, j]*((Qi[j]*P)-(Dij[i,j]*Ck[_])) for i in range(n) for j in range(n)), GRB.MAXIMIZE)
                m.update()
                ####################################
                #constraint
                '''
                constraint of mTSP
                '''
                
                for j in range(1,n):
                        m.addConstr(quicksum(X[i,j]for i in range(n)) <= 1)#sum of incoming links to j <=1
                for i in range(1,n):
                        m.addConstr(quicksum(X[i,j]for j in range(n)) <= 1)#sum of outgoing links from i <=1
                
                m.addConstr(quicksum(X[0,i] for i in range(1,n)) == me)#two salesman start from 0
                m.addConstr(quicksum(X[i,0] for i in range(1,n)) == me)#two salesman end to 0
                
                '''
                MTZ sub tour elim
                '''
                for i in range(1,n):
                    m.addConstr(uX[i]+(L-2)*X[0,i]-X[i,0]<=L-1)
                    m.addConstr(uX[i]+X[0,i]+(2-K)*X[i,0]>=2)
                    for j in range(1,n):
                        if i!=j:
                            m.addConstr(uX[i]-uX[j]+L*X[i,j]+(L-2)*X[j,i]<=L-1)
                
                for i in range(1,n):
                    m.addConstr(X[0,i] + X[i,0] <=1)
                '''
                time constriant
                '''
                m.addConstr(quicksum(X[i,j]*Dij[i,j]/1000 for i in range(n)for j in range(n))<=T*Vk[_])
                '''
                one in one out except Entry
                '''
                for j in range(1,n):
                    for k in range(n):
                        m.addConstr((X[k,j]==1)>>(quicksum(X[j,i]for i in range(n))==1))
                '''
                vehicle capacity constraint
                '''
                m.addConstr(quicksum(X[i,j]*Qi[j]for i in range(n)for j in range(n))<=Pk[_])
                
                m.update()
        
        ############################################################################################     
                m.optimize()          
                
                if m.status == GRB.Status.OPTIMAL:
                    print ('objective: %f' % m.ObjVal)
                    if m.ObjVal <0:
                        print('delivery by '+'{}'.format(vehicle[_])+' is not profitable')
                        
                    else: 
                        plt.xlabel("X")
                        plt.ylabel("Y")
                        plt.title("Route_"+'{}'.format(vehicle[_])) 
                        solution = m.getAttr('x', X)
                        for i in range(n):
                                   plt.scatter(coordinate[i,0],coordinate[i,1],color='green') 
                                   for j in range(n):
                                       if solution[i,j] > 0.5:
                                           print('%s -> %s: %g' % (i, j, solution[i,j]))
                                           plt.arrow(coordinate[i,0],coordinate[i,1],(coordinate[j,0]-coordinate[i,0]),(coordinate[j,1]-coordinate[i,1]),head_length=200,
                                                     head_width=330,width=30,color='red',length_includes_head=True)
                        plt.show()                  
                else:
                    print("it's not optimal ")
                print()        
      

def ReadXlsx(path,i):
    file = pd.read_excel(path)
    print(file)
    file = np.array(file)
    if i ==1:#DistanceMatrix
        file=file[:,1:]
    if i ==2:#VirtualDemand
        file=file[:,3]
        file=np.delete(file,0)
    if i ==3:#Coordinate
        file = file
    return file
if __name__ == '__main__':
    main()
   
#https://www.scitepress.org/papers/2018/65492/65492.pdf
#https://www.gushiciku.cn/pl/p3hL/zh-tw
#https://ozgurakgun.github.io/ModRef2017/files/ModRef2017_MTSP.pdf
