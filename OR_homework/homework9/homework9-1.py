from gurobipy import *
m = Model("homework9_1")
m.setParam('OutputFlag', False)
x1 = m.addVar(vtype ='B', name="x1")
x2 = m.addVar(vtype ='B', name="x2")
x3 = m.addVar(vtype ='B', name="x3")
x4 = m.addVar(vtype ='B', name="x4")
m.update()

z_feasible = 0


terminate = False

while terminate == False:
    u1 = input('u1 upper bound is :')
    u2 = input('u2 upper bound is :')
    gap =[]
    Z  =[]
    Zu =[]
    U1 =[]
    U2 =[]
    for i in range (int(u1)):
        for j in range (int(u2)):
            
            m.setObjective(16*x1 + 10*x2 + 4*x4 + i*(1-x1-x2)+j*(1-x3-x4),GRB.MAXIMIZE)
            m.addConstr(8*x1 + 2*x2 + x3 + 4*x4 <= 10)
            m.optimize()
            
            if 8*x1.x + 2*x2.x + x3.x + 4*x4.x > 10:
                z_feasible =0
            else:
                z_feasible = 16*x1.x + 10*x2.x + 4*x4.x 
            
            if x1.x + x2.x > 1 or x3.x + x4.x > 1:
                z_feasible =0
            else:
                if m.objVal == z_feasible:
                    terminate = True
            if z_feasible !=0:
                U1.append(i)
                U2.append(j)
                gap.append((m.objval-z_feasible)/z_feasible)
                Z.append(z_feasible)
                Zu.append(m.objval)
    if terminate == False:
        print ('Not feasible ','Please choose higher u1,u2 bound ')
               
tmp = min(gap)
index = gap.index(tmp)
print('u1 = ',U1[index])
print('u2 = ',U2[index])
print('gap = ', gap[index],'%')
print('Z= ',Z[index])
print('Zu= ',Zu[index])
