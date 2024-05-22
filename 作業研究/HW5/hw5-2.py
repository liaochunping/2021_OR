

from gurobipy import *

'''
A無上限所以設10000
'''
s = [50, 75]
d = [75, 50]
p = [10000, 60, 70]

'''
Transport Costs 
swc=S到W的cost ABC依序
sdc wdc以此類推
wc是Warehouse Capacities and Costs(1-year)
'''
swc = [[1, 2, 8], [6, 3, 1]]
sdc = [[4, 8], [7, 6]]
wdc = [[4, 6], [3, 4], [5, 3]]
wc = [50, 60, 68]

m = Model("lp1")

'''
w是開哪間
a是supply to warehouse
bc以此類推
'''
w = m.addVars(3, vtype=GRB.BINARY,name="open")
a = m.addVars(2, 3, vtype=GRB.INTEGER, name="supply to warehouse")
b = m.addVars(2, 2, vtype=GRB.INTEGER, name="supply to demand")
c = m.addVars(3, 2, vtype=GRB.INTEGER, name="warehouse to demand")
m.update()

m.setObjective(a[0, 0] * swc[0][0] + a[0, 1] * swc[0][1] + a[0, 2] * swc[0][2] +
               a[1, 0] * swc[1][0] + a[1, 1] * swc[1][1] + a[1, 2] * swc[1][2] +
               b[0, 0] * sdc[0][0] + b[0, 1] * sdc[0][1] +
               b[1, 0] * sdc[1][0] + b[1, 1] * sdc[1][1] +
               c[0, 0] * wdc[0][0] + c[0, 1] * wdc[0][1] +
               c[1, 0] * wdc[1][0] + c[1, 1] * wdc[1][1] +
               c[2, 0] * wdc[2][0] + c[2, 1] * wdc[2][1] +
               w[0] * wc[0] + w[1] * wc[1] + w[2] * wc[2], GRB.MINIMIZE)
'''
w的限制式
'''
m.addConstr(w.sum() == 1)
m.addConstrs(a.sum('*',j) <= w[j] * p[j]  for j in range(0, 3))
m.addConstrs(c.sum(j,'*') <= w[j] * p[j]  for j in range(0, 3))
m.addConstrs(a.sum('*', j) >= c.sum(j, '*') for j in range(0, 3))
'''
S的限制式
'''
m.addConstrs(a.sum(i, '*') + b.sum(i, '*') <= s[i] for i in range(0, 2))
'''
D的限制式
'''
m.addConstrs(b.sum('*', k) + c.sum('*', k) >= d[k] for k in range(0, 2))

m.optimize()

for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))
print('Obj: %f' % m.objVal)