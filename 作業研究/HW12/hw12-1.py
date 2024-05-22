# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 01:19:14 2020

@author: User
"""

from gurobipy import*

m = gurobipy.Model()

c = [[3, 9, 3, 2],
     [9, 4, 10, 3],
     [8, 6, 4, 5]]

x = m.addVars( 3, 4,vtype=GRB.BINARY, name="x")

m.update()

m.setObjective(quicksum(c[i][j]*x[i,j] for i in range(3) for j in range(4)),GRB.MAXIMIZE)

for i in range(3):
    m.addConstr(quicksum(x[i,j]for j in range(4))<=1)
for j in range(4):
    m.addConstr(quicksum(x[i,j]for i in range(3))<=1)
    
m.setParam('OutputFlag',0)
m.optimize()

for v in m.getVars():
        print('%s: %f' % (v.varName, v.x))