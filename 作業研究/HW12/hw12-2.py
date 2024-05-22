
from gurobipy import*

m = gurobipy.Model()


cost = [[8, 6, 10, 9],
        [9, 12, 13, 7],
        [14, 9, 16, 5]]


supply = [35,50,40]
demand = [45,20,30,30]

x = m.addVars( 3, 4, vtype=GRB.INTEGER,name ='x')

m.update()

m.setObjective(quicksum(cost[i][j]*x[i,j] for i in range(3) for j in range(4)),GRB.MINIMIZE)

for i in range(3):
    m.addConstr(quicksum(x[i,j]for j in range(4))<=supply[i])
for j in range(4):
    m.addConstr(quicksum(x[i,j]for i in range(3))>=demand[j])

m.setParam('OutputFlag',0)
m.optimize()


print ('Optimal flows:')


for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))

