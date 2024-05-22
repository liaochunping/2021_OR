
from gurobipy import *
def addConstr(n):    
    if n ==1:
        return 
    if n ==2:
        return m.addConstr( x2  >= 6, "c2") 
    if n ==3:
        return m.addConstr( x2  >= 6, "c2") ,m.addConstr( x1  <= 1, "c3")
    if n ==4:
        return m.addConstr( x2  >= 6, "c2") ,m.addConstr( x1  <= 1, "c3"),m.addConstr( x2  <= 6, "c4")
    if n ==5:
        return m.addConstr( x2  >= 6, "c2") ,m.addConstr( x1  <= 1, "c3"),m.addConstr( x2  >= 7, "c4")
    if n ==6:
        return m.addConstr( x2  >= 6, "c2") ,m.addConstr( x1  >= 2, "c3")
    if n ==7:
        return m.addConstr( x2  <= 5, "c2")
    
for _ in range(7):
    print(_+1)
    m = Model("LP")
    x1 = m.addVar( name="x1")
    x2 = m.addVar( name="x2")
    m.setObjective(2*x1 + 3*x2 , GRB.MAXIMIZE)
    m.addConstr(2* x1 +  1* x2 <= 10, "c0")
    m.addConstr( 15 * x1 + 30 * x2 <= 200, "c1")
    m.addConstr(x1 >= 0)
    m.addConstr(x2 >= 0)
    addConstr(_+1)
    m.update()
    m.setParam( 'OutputFlag', False )
    m.optimize()
    if m.status == GRB.OPTIMAL:
        print('Optimal objective: %g' % m.objVal)
    elif m.status == GRB.INF_OR_UNBD:    
        print('Model is infeasible or unbounded')
        continue
    elif m.status == GRB.INFEASIBLE:    
        print('Model is infeasible')
        continue
    elif m.status == GRB.UNBOUNDED:    
        print('Model is unbounded')    
        continue
    else:    
        print('Optimization ended with status %d' % m.status)    
        continue
    for v in m.getVars():
        print('%s: %f' % (v.varName, v.x))
    

