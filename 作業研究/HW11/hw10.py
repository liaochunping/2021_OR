import knapsackDP as dp
import numpy as np
from gurobipy import *

N = 4
L = 100

li = [45, 36, 31, 14]
d = [97, 610, 395, 211]

types = []
for i in range(N):
    types.append([])
    for j in range(N):
        if i == j:
            types[i].append(1)
        else:
            types[i].append(0)

x = {}
c = {}
pi = []
constlist = []
index = 0

m = Model("CSP")
m.setParam( 'OutputFlag', False )

for i in range(N):
    x[i] = m.addVar(name="type_%d" % i)
    index += 1
    
m.setObjective(quicksum(x[i] for i in range(N)), GRB.MINIMIZE)
m.update()

for i in range(N):
    c[i] = m.addConstr(x[i] >= d[i])
    constlist.append(c[i])
    pi.append(0.0)
    
m.optimize()

for i in range(N):
    pi[i] = c[i].pi

obj, result = 1-dp.knapsackDP(L, li, pi).f, dp.knapsackDP(L, li, pi).result
types.append(result)

while(True):
    col = Column(result, constlist)
    x[index] = m.addVar(name="type_%d" % index, column=col)
    m.update()
    m.setObjective(quicksum(x[i] for i in range(index+1)))
    m.optimize()

    for i in range(N):
        pi[i] = c[i].pi

    obj, result = 1 - dp.knapsackDP(L, li, pi).f, dp.knapsackDP(L, li, pi).result
    if obj >= 0:
        break
    types.append(result)

    index += 1

branch = False

for i in range(index + 1):
    if abs(math.floor(x[i].x) - x[i].x) > 0.0001:
        branch = True

if branch:
    for i in range(index + 1):
        x[i].vtype = 'I'
        
    m.optimize()

dp.output_matrix(types)
dp.output(m)