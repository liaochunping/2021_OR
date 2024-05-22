# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:27:13 2019

@author: User
"""
from gurobipy import*
m = Model("CuttingStock")
length = [45,34,31,14]

x = {}
k = 4
for i in range(k):
    x[i] = m.addVar(name='variables_%s'%i)
m.update()

m.setObjective(quicksum(x[i] for i in range(k)), GRB.MAXIMIZE)

m.addConstr(quicksum(x[i]*length[i] for i in range(k))<=100)

m.optimize()

print('Obj: %f' % m.objVal)

