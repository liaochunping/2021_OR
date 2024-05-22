
from gurobipy import *
m = Model("lp1")
x1 = m.addVar(name="x1")
x2 = m.addVar(name="x2")

m.update()
m.setObjective(5*x1 + 4*x2 , GRB.MAXIMIZE)

m.addConstr(6*x1 + 4*x2  <= 24, "st1")
m.addConstr(x1 + 2*x2  <= 6, "st2")
m.addConstr(-1*x1 + x2  <= 1, "st3")
m.addConstr(x2 <= 2, "c_demand")
m.addConstr(x1 >= 0)
m.addConstr(x2 >= 0)
m.optimize()
print()
print('End of gurobis shits ')
for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))
print('Obj: %f' % m.objVal)
print ('reduced costs: ')
print (' ', m.getAttr('rc', m.getVars()))
print ('shadow prices: ')
print (' ', m.getAttr('pi', m.getConstrs()))