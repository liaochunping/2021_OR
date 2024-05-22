# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 00:57:20 2019

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

# Create optimization model
m = Model('TSP')
# Create variables
x = {}
u = {}
arcs, cost = multidict(cost)

x['Detroit','Boston'] =m.addVar(obj=cost['Detroit','Boston'],
             vtype = 'B', name='x_%s%s' % ('Detroit', 'Boston'))
x['Detroit','New York'] =m.addVar(obj=cost['Detroit','New York'],
             vtype = 'B', name='x_%s%s' % ('Detroit','New York'))
x['Detroit','Seattle'] =m.addVar(obj=cost['Detroit','Seattle'],
             vtype = 'B', name='x_%s%s' %('Detroit','Seattle'))

x['Boston','Detroit'] = m.addVar(obj=cost['Boston','Detroit'],
             vtype = 'B', name='x_%s%s' % ('Boston','Detroit'))
x['Boston','New York'] =m.addVar(obj=cost['Boston','New York'],
             vtype = 'B', name='x_%s%s' % ('Boston','New York'))
x['Boston','Seattle'] =m.addVar(obj=cost['Boston','Seattle'],
             vtype = 'B', name='x_%s%s' % ('Boston','Seattle'))

x['New York','Detroit'] =m.addVar(obj=cost['New York','Detroit'],
             vtype = 'B', name='x_%s%s' % ('New York','Detroit'))
x['New York','Boston'] =m.addVar(obj=cost['New York','Boston'],
             vtype = 'B', name='x_%s%s' % ('New York','Boston'))
x['New York','Seattle'] =m.addVar(obj=cost['New York','Seattle'],
             vtype = 'B', name='x_%s%s' % ('New York','Seattle'))

x['Seattle','Detroit'] =m.addVar(obj=cost['Seattle','Detroit'],
             vtype = 'B', name='x_%s%s' % ('Seattle','Detroit'))
x['Seattle','Boston'] =m.addVar(obj=cost['Seattle','Boston'],
             vtype = 'B', name='x_%s%s' % ('Seattle','Boston'))
x['Seattle','New York'] =m.addVar(obj=cost['Seattle','New York'],
             vtype = 'B', name='x_%s%s' % ('Seattle','New York'))

N = len(nodes)

u['Detroit'] = m.addVar(obj=0, name='u_%s' % 'Detroit')
u['Boston'] = m.addVar(obj=0, name='u_%s' % 'Boston')
u['New York'] = m.addVar(obj=0, name='u_%s' % 'New York')

m.update()

# Constraint for sum of incoming links to j
m.addConstr(x['Boston','Detroit']+x['New York','Detroit']
    +x['Seattle','Detroit'] == 1, 'incom_%s' % ('Detroit'))
m.addConstr(x['Detroit','Boston']+x['New York','Boston']
    +x['Seattle','Boston'] == 1, 'incom_%s' % ('Boston'))
m.addConstr(x['Detroit','New York']+x['Boston','New York']
    +x['Seattle','New York'] == 1, 'incom_%s' % ('New York'))
m.addConstr(x['Detroit','Seattle']+x['Boston','Seattle']
    +x['New York','Seattle'] == 1,'incom_%s' % ('Seattle'))

# Constraint for sum of outgoing links from i
m.addConstr(x['Detroit','Boston']+x['Detroit','New York']
    +x['Detroit','Seattle'] == 1, 'outgo_%s' % ('Detroit'))
m.addConstr(x['Boston','Detroit']+x['Boston','New York']
    + x['Boston','Seattle'] == 1, 'outgo_%s' % ('Boston'))
m.addConstr(x['New York','Detroit']+x['New York','Boston']
    + x['New York','Seattle'] == 1,'outgo_%s' % ('New York'))
m.addConstr(x['Seattle','Detroit']+x['Seattle','Boston']
    + x['Seattle','New York'] == 1, 'outgo_%s' % ('Seattle'))

# Subtour elimination constraints
m.addConstr(u['Detroit']-u['Boston']
    +N*x['Detroit','Boston'] <= N-1,
        'subtour_%s_%s' % ('Detroit', 'Boston'))
m.addConstr(u['Detroit'] - u['New York']
    +N*x['Detroit','New York'] <= N-1,
        'subtour_%s_%s' % ('Detroit', 'New York'))
m.addConstr(u['Boston'] - u['Detroit']
    +N*x['Boston','Detroit'] <= N-1,
        'subtour_%s_%s' % ('Boston', 'Detroit'))

# Subtour elimination constraints continue
m.addConstr(u['Boston'] - u['New York']
    +N*x['Boston','New York'] <= N-1,
        'subtour_%s_%s' % ('Boston', 'New York'))
m.addConstr(u['New York'] - u['Detroit']
    +N*x['New York','Detroit'] <= N-1,
        'subtour_%s_%s' % ('New York', 'Detroit'))
m.addConstr(u['New York'] - u['Boston']
    +N*x['New York','Boston'] <= N-1,
        'subtour_%s_%s' % ('New York', 'Boston'))

# Compute optimal solution
m.optimize()
# Print solution
if m.status == GRB.Status.OPTIMAL:
    print 'objective: %f' % m.ObjVal
    solution = m.getAttr('x', x)
    for i,j in arcs:
        if solution[i,j] > 0:
            print('%s -> %s: %g' % (i, j, solution[i,j]))


