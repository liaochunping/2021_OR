# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:57:28 2019

@author: User
"""
from gurobipy import *
m = Model("IPExample")



x1 = m.addVar( name="x1", obj = 8)
x2 = m.addVar( name="x2", obj = 5)

m.setAttr('ModelSense', GRB.MAXIMIZE)

m.update()

m.addConstr(9 * x1 + 5 * x2 <= 45, "c0")
m.addConstr( 1 * x1 + 1 * x2 <= 6, "c1")

m.setParam( 'OutputFlag', False )

m.optimize()

i = 1

print('node' + str(i) )
for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))
print('Obj: %f' % m.objVal)


for i in range(1) :
    
    x = m.addVars(i)
    
    if x.isdigit() == true :
        
        x = int(x)
        
        
        
        i-=1
    else:
        
        x = m.addVars(i)
        n = int(x1)
        
        m.addConstr( x[i]  >= n, "c3")
        
        m.optimize()
        print('node' + str(i) )
        for v in m.getVars():
            print('%s: %f' % (v.varName, v.x))
        print('Obj: %f' % m.objVal)
        
        i +=1
    
       
