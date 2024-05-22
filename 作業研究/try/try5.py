# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:17:06 2019

@author: User
"""
from gurobipy import *

m = Model("lp1")
x1 = m.addVar(name="x1")
x2 = m.addVar(name="x2")
x3 = m.addVar(name="x3")
m.update()
m.setObjective(500*x1 + 450*x2 + 600*x3, GRB.MAXIMIZE)
m.addConstr(6*x1 + 5*x2 + 8*x3 <= 60, "c_production")
m.addConstr(10*x1 + 20*x2 + 10*x3 <= 150, "c_storage")
m.addConstr(x1 <= 8, "c_demand")
m.optimize()

for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))
print('Obj: %f' % m.objVal)
print 'reduced costs: '
print ' ', m.getAttr('rc', m.getVars())
print 'shadow prices: '
print ' ', m.getAttr('pi', m.getConstrs())