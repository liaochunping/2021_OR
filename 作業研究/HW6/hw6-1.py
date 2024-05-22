
from gurobipy import *

cost = [[0      ,2429   ,1967   ,1497   ,1650   ,2392   ],
        [2429   ,0      ,1105   ,1674   ,1320   ,5566   ],
        [1967   ,1105   ,0      ,2023   ,9527   ,560    ],
        [1497   ,1674   ,2023   ,0      ,1999   ,1273   ],
        [1650   ,1320   ,9527   ,1999   ,0      ,778    ],
        [2392   ,5566   ,560    ,1273   ,778    ,0      ]]



# Create optimization model
m = Model('TSP')
# Create variables
x = {}
u = {}
n = len(cost)

for i in range(n):
    for j in range(n):
        x[i, j] = m.addVar(obj=cost[i][j], vtype = 'B', name = 'x_%d%d' %(i, j))


for i in range(n):
    if i != n-1:
        u[i] = m.addVar(obj=0, name='u_%s' % i)

m.update()

# Constraint for sum of incoming links to j
for j in range(n):
    m.addConstr(quicksum(x[i,j]
        for i in range(n) if i != j) == 1,
            'incom_%s' % (j))

# Constraint for sum of outgoing links from i
for i in range(n):
    m.addConstr(quicksum(x[i,j]
        for j in range(n) if i != j) == 1,
            'outgo_%s' % (i))

# Subtour elimination constraints
for i in range(n):
    for j in range(n):
        if i != n-1 and j != n-1:
            m.addConstr(u[i] - u[j] + n*x[i,j] <= n-1,
                    'subtour_%s_%s' % (i, j))

# Compute optimal solution
m.optimize()
# Print solution
if m.status == GRB.Status.OPTIMAL:
    print ('objective: %f' % m.ObjVal)
    solution = m.getAttr('x', x)
    for i in range(n):
        for j in range(n):
            if solution[i,j] > 0:
                print('%s -> %s: %g' % (i, j, solution[i,j]))