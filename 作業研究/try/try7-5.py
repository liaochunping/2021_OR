from gurobipy import *
m = Model("IPExample")

x1 = m.addVar( name="x1", obj = 8)
x2 = m.addVar( name="x2", obj = 5)

m.setAttr('ModelSense', GRB.MAXIMIZE)

m.update()

m.addConstr(9 * x1 + 5 * x2 <= 45, "c0")
m.addConstr( 1 * x1 + 1 * x2 <= 6, "c1")

m.setParam( 'OutputFlag', False )

m.optimize()


i = 1
p = x1.x
q = x2.x
    
    if (p - int(p)!=0)  :
        a = int(p)
        b = int(p)+1
        
    elif(q - int(q)!=0):
        
       
    else:
        print('node' + str(i) )
        for v in m.getVars():
            print('%s: %f' % (v.varName, v.x))
        print('Obj: %f' % m.objVal)
      

