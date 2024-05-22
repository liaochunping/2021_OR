# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 01:32:42 2019

@author: User
"""

from gurobipy import *
m = Model("IPExample")

x1 = m.addVar(vtype=GRB.INTEGER, name="x1", obj = 17)
x2 = m.addVar(vtype=GRB.INTEGER, name="x2", obj = 12)

m.setAttr('ModelSense', GRB.MAXIMIZE)
# Variables and attributes are set in a lazy fashion
# in Gurobi. You need to update() to make it effective.
m.update()
m.addConstr(10 * x1 + 7 * x2 <= 40, "c0")
m.addConstr( 1 * x1 + 1 * x2 <= 5, "c1")

m.setParam( 'OutputFlag', False )
m.optimize()
print('Optimal from MIP solver:')
for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))
print('Obj: %f' % m.objVal)
