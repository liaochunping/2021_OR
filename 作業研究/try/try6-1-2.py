

from gurobipy import *

nodes = ['Detroit', 'Boston', 'New York', 'Seattle','New City','Home City']
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
        ('Seattle','New York'): 2023,
        ('Detroit', 'New City'): 1650,
        ('Detroit', 'Home City'): 2392,
        ('Boston', 'New City'): 1320,
        ('Boston', 'Home City'): 5566,
        ('New York','New City'): 9527,
        ('New York','Home City'): 560,
        ('Seattle','New City'): 1999,
        ('Seattle','Home City'): 1273,
        ('New City','Home City'): 778,
        ('Home City','New City'): 778,
        ('New City','Detroit'): 1650,
        ('New City','Boston'): 1320,
        ('New City','New York'): 9527,
        ('New City','Seattle'): 1999,
        ('Home City','Detroit'): 2392,
        ('Home City','Boston'): 5566,
        ('Home City','New York'): 560,
        ('Home City','Seattle'): 1273,
        }


arcs, cost = multidict(cost)

# Create optimization model
m = Model('TSP')
# Create variables
x = {}
u = {}
N = len(nodes)

for i,j in arcs:
    x[i,j] = m.addVar(obj=cost[i,j], vtype = 'B',
         name='x_%s%s' % (i, j))

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















