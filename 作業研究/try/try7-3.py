# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:42:46 2019

@author: User
"""

from gurobipy import *
m = Model("IPExample")

x1 = m.addVar( name="x1", obj = 8)
x2 = m.addVar( name="x2", obj = 5)

m.setAttr('ModelSense', GRB.MAXIMIZE)
# Variables and attributes are set in a lazy fashion
# in Gurobi. You need to update() to make it effective.
m.update()
m.addConstr(9 * x1 + 5 * x2 <= 45, "c0")
m.addConstr( 1 * x1 + 1 * x2 <= 6, "c1")

#用來算枚舉數的限制式
m.addConstr( x1  <= 3, "c2")

m.setParam( 'OutputFlag', False )

m.optimize()
print('Optimal from MIP solver:')
for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))
print('Obj: %f' % m.objVal)

