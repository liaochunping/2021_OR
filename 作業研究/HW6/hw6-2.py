# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 02:01:28 2019

@author: User
"""

from gurobipy import *

'''
設supply跟demand
'''
s = [15, 20]
d = [17, 8,10]

'''
Transport Costs 
pmc=S到W的cost ABC依序
'''
pmc = [[3,4,6], [5,7,5]]

m = Model("lp1")

'''
b是port to market
'''


b = m.addVars(2, 3, vtype=GRB.INTEGER, name="port to market")

m.update()

m.setObjective(b[0, 0] * pmc[0][0] + b[0, 1] * pmc[0][1] + b[0, 2] * pmc[0][2] +
               b[1, 0] * pmc[1][0] + b[1, 1] * pmc[1][1] + b[1, 2] * pmc[1][2] 
               , GRB.MINIMIZE)

'''
S的限制式
'''
m.addConstrs(b.sum(i, '*') <= s[i] for i in range(0, 2))
'''
D的限制式
'''
m.addConstrs(b.sum('*', k) >= d[k] for k in range(0, 3))

m.optimize()

for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))
print('Obj: %f' % m.objVal)