# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 22:28:25 2019

@author: User
"""

from gurobipy import *


m = Model("m1")
m.setParam('OutputFlag', False)
x1 = m.addVar(vtype ='B', name="x1")
x2 = m.addVar(vtype ='B', name="x2")
x3 = m.addVar(vtype ='B', name="x3")
x4 = m.addVar(vtype ='B', name="x4")

m.update()

m.addConstr(8*x1 + 2*x2 + x3 + 4*x4 <= 10)

z_feasible = 0


terminate = False

while terminate == False:
    u1 = input('u1 :')
    u2 = input('u2 :')
    
    m.setObjective(16*x1 + 10*x2 + 4*x4 + u1*(1-x1-x2)+u2*(1-x3-x4),GRB.MAXIMIZE)
    m.addConstr(8*x1 + 2*x2 + x3 + 4*x4 <= 10)
    m.optimize()
    
    if 8*x1.x + 2*x2.x + x3.x + 4*x4.x > 10:
        z_feasible =0
    else:
        z_feasible = 16*x1.x + 10*x2.x + 4*x4.x 
    
    if x1.x + x2.x > 1 or x3.x + x4.x > 1:
        z_feasible =0
        pass
        
    else:
        if m.objVal == z_feasible:
            terminate = True
    
    for i in m.getVars():
        print('%s: %f' % (i.varName, i.x))
    print ('Z* = ',z_feasible)
    print ('Zu = ',m.objval)
    
    if z_feasible !=0:
        print ('gap:', (m.objval-z_feasible)/z_feasible,'%')
    else:
        print ('gap: undefined')
    