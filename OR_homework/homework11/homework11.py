import homework10 as dp
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
#m.setParam( 'OutputFlag', False )

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
obj, result = knapsackDP(L, li, pi)
obj = 1-obj
types.append(result)

while(True):
    col = Column(result, constlist)
    x[index] = m.addVar(name="type_%d" % index, column=col)
    m.update()
    m.setObjective(quicksum(x[i] for i in range(index+1)))
    m.optimize()

    for i in range(N):
        pi[i] = c[i].pi

    obj, result = knapsackDP(L, li, pi)
    obj = 1-obj
    if obj >= 0:
        break
    types.append(result)

    index += 1

branch = False

for i in range(index + 1):
    if abs(math.floor(x[i].x) - x[i].x) > 0.00000000000001:
        branch = True

if branch:
    for i in range(index + 1):
        x[i].vtype = 'I'
        
    m.optimize()
    
for i in range(len(types)):
        for j in range(len(types[0])):
            print(types[i][j],',',end = '')
        print("type_",i)
print("")
if m.getAttr('status') != 2:
        print(m.getAttr('status'))
else:
        for x in m.getVars():
            if x.x != 0:
                print ("%s: %f" % (x.varName, x.x))
        print('Obj: %f' % m.objVal)