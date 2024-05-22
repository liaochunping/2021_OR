#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:11:37 2019

@author: annieliu
"""

from gurobipy import *

cost = {('P1', 'M1'):3, ('P1', 'M2'):4, ('P1', 'M3'):6,
        ('P2', 'M1'):5, ('P2', 'M2'):7, ('P2', 'M3'):5}


# Create optimization model
m = Model('lp1')
# Create variables
x = {}
arcs, n = multidict(cost)

#demand: M1=17, M2=8, M3=10
#supply: P1=15, P2=20
d = {'M1':17, 'M2':8, 'M3':10}
s = {'P1':15, 'P2':20}
for i, j in arcs:
    x[i, j] = m.addVar(vtype=GRB.INTEGER, name = 'x_%s%s' %(i, j))

m.update()

m.setObjective(quicksum(x[i, j] * cost[i, j] for i, j in arcs), GRB.MINIMIZE)

for i in s:
    m.addConstr(quicksum(x[i, j] for j in d) <= s[i], name = 's_%s' %i)
for j in d:
    m.addConstr(quicksum(x[i, j] for i in s) >= d[j], name = 'd_%s' %j)
    
m.optimize()

for v  in m.getVars():
    print('%s = %f' % (v.varName, v.x))

print('z = %f' % m.objVal)