
from gurobipy import*

m = gurobipy.Model()

plants = ['Cleveland','Chicago','Boston']
distribution_centers = ['Dallas','Atlanta','SanFrancisco','Phila']

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

'''
x.setAttr = {"Cleveland -> Dallas", x[0,0]}
x.setAttr = { "Cleveland -> Atlanta",x[0,1] }
x.setAttr = {"Cleveland -> SanFrancisco", x[0,2]}
x.setAttr = { "Cleveland -> Phila",x[0,3]}
x.setAttr = {"Chicago -> Dallas", x[1,0]}
x.setAttr = { "Chicago -> Atlanta", x[1,1]}
x.setAttr = { "Chicago -> SanFrancisco", x[1,2]}
x.setAttr = { "Chicago -> Phila", x[1,3]}
x.setAttr = { "Boston -> Dallas", x[2,0]}
x.setAttr = { "Boston -> Atlanta", x[2,1]}
x.setAttr = { "Boston -> SanFrancisco", x[2,2]}
x.setAttr = { "Boston -> Phila", x[2,3] }
'''

print ('Optimal flows:')


for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))


for f in plants:
    for v in m.getVars():
      print(f,'>',': %f' % (v.x))
