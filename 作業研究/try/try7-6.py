
from gurobipy import *

def output(i):
    if i.getAttr('status') != 2:
        print(i.getAttr('status'))
        print("")
    else:
        for x in i.getVars():
            print ("%s: %f" % (x.varName, x.x))
        print('Obj: %f' % i.objVal)
        print("")

for i in range(1):
    
    m = Model("m1")
    x1 = m.addVar(obj=8, name="x_1")
    x2 = m.addVar(obj=5, name="x_2")
    m.ModelSense = GRB.MAXIMIZE
    m.update()
    m.addConstr(x1 + x2 <= 6, name="c_0")
    m.addConstr(9*x1 + 5*x2 <= 45, name="c_1")
    
    m.addConstr(x1 <= 3)
    
    m.setParam('OutputFlag', False)
    m.optimize()
    print("m")
    output(m)