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


m = Model("m1")
x1 = m.addVar(obj=8, name="x_1")
x2 = m.addVar(obj=5, name="x_2")
m.ModelSense = GRB.MAXIMIZE
m.update()
m.addConstr(x1 + x2 <= 6, name="c_0")
m.addConstr(9*x1 + 5*x2 <= 45, name="c_1")
m.setParam('OutputFlag', False)
m.optimize()
print("m")
output(m)

m1 = Model("m2")

x1 = m1.addVar(obj=8, name="x_1")
x2 = m1.addVar(obj=5, name="x_2")
m1.ModelSense = GRB.MAXIMIZE
m1.update()
m1.addConstr(x1 + x2 <= 6, name="c_0")
m1.addConstr(9*x1 + 5*x2 <= 45, name="c_1")

m1.addConstr(x1 <= 3)

m1.setParam('OutputFlag', False)
m1.optimize()
print("m1")
output(m1)

m2 = Model("m3")
x1 = m2.addVar(obj=8, name="x_1")
x2 = m2.addVar(obj=5, name="x_2")
m2.ModelSense = GRB.MAXIMIZE
m2.update()
m2.addConstr(x1 + x2 <= 6, name="c_0")
m2.addConstr(9*x1 + 5*x2 <= 45, name="c_1")

m2.addConstr(x1 >= 4)

m2.setParam('OutputFlag', False)
m2.optimize()
print("m2")
output(m2)

m21 = Model("m31")
x1 = m21.addVar(obj=8, name="x_1")
x2 = m21.addVar(obj=5, name="x_2")
m21.ModelSense = GRB.MAXIMIZE
m21.update()
m21.addConstr(x1 + x2 <= 6, name="c_0")
m21.addConstr(9*x1 + 5*x2 <= 45, name="c_1")
m21.addConstr(x1 >= 4)
m21.addConstr(x2 >= 2)
m21.setParam('OutputFlag', False)
m21.optimize()
print("m21")
output(m21)

m22 = Model("m32")
x1 = m22.addVar(obj=8, name="x_1")
x2 = m22.addVar(obj=5, name="x_2")
m22.ModelSense = GRB.MAXIMIZE
m22.update()
m22.addConstr(x1 + x2 <= 6, name="c_0")
m22.addConstr(9*x1 + 5*x2 <= 45, name="c_1")
m22.addConstr(x1 >= 4)
m22.addConstr(x2 <= 1)
m22.setParam('OutputFlag', False)
m22.optimize()
print("m22")
output(m22)

m221 = Model("m32")
x1 = m221.addVar(obj=8, name="x_1")
x2 = m221.addVar(obj=5, name="x_2")
m221.ModelSense = GRB.MAXIMIZE
m221.update()
m221.addConstr(x1 + x2 <= 6, name="c_0")
m221.addConstr(9*x1 + 5*x2 <= 45, name="c_1")
m221.addConstr(x1 >= 4)
m221.addConstr(x2 <= 1)
m221.addConstr(x1 >= 5)
m221.setParam('OutputFlag', False)
m221.optimize()
print("m221")
output(m221)

m222 = Model("m32")
x1 = m222.addVar(obj=8, name="x_1")
x2 = m222.addVar(obj=5, name="x_2")
m222.ModelSense = GRB.MAXIMIZE
m222.update()
m222.addConstr(x1 + x2 <= 6, name="c_0")
m222.addConstr(9*x1 + 5*x2 <= 45, name="c_1")
m222.addConstr(x1 >= 4)
m222.addConstr(x2 <= 1)
m222.addConstr(x1 <= 4)
m222.setParam('OutputFlag', False)
m222.optimize()
print("m222")
output(m222)
