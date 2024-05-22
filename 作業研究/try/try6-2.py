# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 01:19:52 2019

@author: User
"""

from gurobipy import *

nodes = ['Detroit', 'Boston', 'New York', 'Seattle']
cost = {
        ('Detroit', 'Boston'): 2429,
        ('Detroit', 'New York'): 1967,
        ('Detroit', 'Seattle'): 1497,
        ('Boston', 'Detroit'): 2497,
        ('Boston', 'New York'): 1105,
        ('Boston', 'Seattle'): 1674,
        ('New York','Detroit'): 1967,
        ('New York','Boston'): 1105,
        ('New York','Seattle'): 2023,
        ('Seattle','Detroit'): 1497,
        ('Seattle','Boston'): 1674,
        ('Seattle','New York'): 2023
        }

arcs, cost = multidict(cost)
# Create optimization model
m = Model('TSP')
# Create variables
x = {}
u = {}

for i,j in arcs:
    x[i,j] = m.addVar(obj=cost[i,j], vtype = 'B',
         name='x_%s%s' % (i, j))

N = len(nodes)

for i in nodes:
    if i != nodes[N-1]:
        u[i] = m.addVar(obj=0, name='u_%s' % i)

m.update()

# Constraint for sum of incoming links to j
for j in nodes:
    m.addConstr(quicksum(x[i,j]
        for i in nodes if i != j) == 1,
            'incom_%s' % (j))

# Constraint for sum of outgoing links from i
for i in nodes:
    m.addConstr(quicksum(x[i,j]
        for j in nodes if i != j) == 1,
            'outgo_%s' % (i))

# Subtour elimination constraints
for i,j in arcs:
    if i != nodes[N-1] and j != nodes[N-1]:
        m.addConstr(u[i] - u[j] + N*x[i,j] <= N-1,
                    'subtour_%s_%s' % (i, j))

# Compute optimal solution
m.optimize()
# Print solution
if m.status == GRB.Status.OPTIMAL:
    print 'objective: %f' % m.ObjVal
    solution = m.getAttr('x', x)
    for i,j in arcs:
        if solution[i,j] > 0:
            print('%s -> %s: %g' % (i, j, solution[i,j]))







