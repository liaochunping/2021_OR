from gurobipy import*
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
def ReadXlsx(path,i):
    file = pd.read_excel(path)
    file = np.array(file)
    if i ==1:#DistanceMatrix
        file=file[:,1:]
    if i ==2:#VirtualDemand
        file=file[:,3]
        file=np.delete(file,0)
    return file


def subtourelim(model, where):
    if where == GRB.callback.MIPSOL:
        selected = []
        cities = []
        n = model._n
        for i in range(n):
            sol = model.cbGetSolution([model._vars[i,j] for j in range(n)])
            selected += [(i,j) for j in range(n) if sol[j] > 0.5]

        for i in range(len(selected)):
            if selected[i][0] not in cities:
                cities.append(selected[i][0])
            if selected[i][1] not in cities:
                cities.append(selected[i][1])
        print(cities)
        if len(selected) < len(cities) - 1:
            expr = 0
            for edge in selected:
                expr += model._vars[edge[0], edge[1]]
            model.cbLazy(expr == len(cities) - 1)

DEBUG =1
def main():
    #try:
        
        m = Model('Final_project_test')
        
        m.setParam('TimeLimit', 10)
        m.setParam('OutputFlag', True)
        ###################################
        #interger parameters
        Pk =[4,3,2]                       #capacity of vehicle k
        Ck =[1,2,9]                       #cost of vehicle k per unit distance
        Vk =[3,4,5]                       #velocity of a vehcle k
        Dij = ReadXlsx('Distance Matrix.xlsx',1)  #distance between any pair of node i,j 
        P = 30                                  #price of a burger
        Qi = ReadXlsx('Virtual Demand.xlsx',2)    #burger demand of a node
        Tk = [[20],[30],[40]]                   # maximum total travel time allowed for vehicle k
        L = len(Dij)                           #Max number of cities a salesman can visit
        K = 0                                   #Minimum number of cities a salesman can visit
        me = 2                                   #Number of salesmen            
        m.update()
        ###################################
        #Binary variables
        n =len(Dij)             #number of nodes
        k =len(Pk)              #number of vehicles
        X ={}                   #initialize the varibales whether goes from node i to j     
        Um,Ul={},{}             #initialize whether Mario and Luigi use the vehicle k
        uX={}                   #subtour elimation variables for MTZ method
        pa=2                    #to be the maximum number of nodes that can be visited by any salesman
        for i in range(n):
            uX[i]=m.addVar(vtype = 'I',name='u'+str(i)) #subtour elimation
            for j in range(n):
               X[i,j] = m.addVar(vtype ='B' , name='e_'+str(i)+'_'+str(j))
        for i in range(k):
                Um[i] =m.addVar(vtype ='B' , name ='{}'.format('Um',i))
                Ul[i] =m.addVar(vtype ='B' , name ='{}'.format('Ul',i))
       
        ###################################
        #Integer varibales
        Mi ={}              #Mario sells burger at point i
        Li ={}              #Luigi sells burger at point i
        for i in range(n):
            Mi[i] =m.addVar(vtype = 'I', name = '{}'.format('Mi',i))
            Li[i] =m.addVar(vtype = 'I', name = '{}'.format('Li',i))
                    
            
            
        ####################################
        #constraint
        '''
        constraint of mTSP
        '''
        m.setObjective(quicksum(X[i, j] for i in range(n) for j in range(n)), GRB.MAXIMIZE)
        
        for j in range(n):
            if j !=0:
                m.addConstr(quicksum(X[i,j]for i in range(n)) <= 1)#sum of incoming links to j <=2
        for i in range(n):
            if i !=0:
                m.addConstr(quicksum(X[i,j]for j in range(n)) <= 1)#sum of outgoing links from i <=2
       
          
        m.addConstr(quicksum(X[0,i] for i in range(1,n)) == 2)#two salesman start from 0
        m.addConstr(quicksum(X[i,0] for i in range(1,n)) == 2)#two salesman end to 0
        
        for i in range(1,n):
            m.addConstr(uX[i]+(L-2)*X[0,i]-X[i,0]<=L-1)
            m.addConstr(uX[i]+X[0,i]+(2-K)*X[i,0]>=2)
            for j in range(1,n):
                if i!=j:
                    m.addConstr(uX[i]-uX[j]+L*X[i,j]+(L-2)*X[j,i]<=L-1)
        
        for i in range(1,n):
            m.addConstr(X[0,i] + X[i,0] <=1)
        
        
        '''
        one vehicle constriant
        '''
        '''
        m.addConstr(quicksum(Um[i]for i in range(k)) == 1)# Mario pick only one vehicle
        m.addConstr(quicksum(Ul[i]for i in range(k)) == 1)# Luigi pick only one vehicle
        '''
        '''
        node demand constraint
        '''
        for i in range(n):
            m.addConstr(Mi[i]+Li[i]<=Qi[i]) #the burger sells at the node i is smaller equal to the demand
        
        '''
        vehicle capacity constraint
        '''
        m.addConstr(quicksum(Mi[i]for i in range(n))<=quicksum((Pk[i]*Um[i]for i in range(k))))
        m.addConstr(quicksum(Li[i]for i in range(n))<=quicksum((Pk[i]*Ul[i]for i in range(k))))
        
        '''
        time constriant
        '''
        m.addConstr(quicksum(X[i,j]*Dij[i,j] for i in range(n)for j in range(n))<=10000)
        '''
        V = quicksum(Vk[k]*Um[k]for k in range(k))
        T = quicksum(Tk[k]*Um[k]for k in range(k))
        m.addConstr(quicksum(X[i,j]*Dij[i,j] for i in range(n)for j in range(n))<= V * T)
        '''
        for j in range(1,n):
            for k in range(n):
                m.addConstr((X[k,j]==1)>>(quicksum(X[j,i]for i in range(n))==1))
         
            
        
        
        
        
        
        
        
        
        
        
        
        
        m.update()

        
        
        
        
        m.optimize()
       
        '''       
        solution = m.getAttr('x', X)
        selected = [(i,j) for i in range(n) for j in range(n) if solution[i,j] > 0.5]
        
        uValues = m.getAttr('x',uX)
        print("U values: ", uValues)
        
        print('')
        print('Optimal tour: %s' % str(selected))
        print('Optimal cost: %g' % m.objVal)
        print('') 
        '''
           
        print ('objective: %f' % m.ObjVal)
        solution = m.getAttr('x', X)
        for i in range(n):
                   for j in range(n):
                       if solution[i,j] > 0:
                           print('%s -> %s: %g' % (i, j, solution[i,j]))
                           
         
        
        
        
        
        
            
        #except:
            
































        












if __name__ == '__main__':
    main()
   