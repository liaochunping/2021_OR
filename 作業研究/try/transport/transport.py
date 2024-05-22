from gurobipy import *

try:

    factories = ['Cleveland','Chicago','Boston']

    stores = ['Dallas','Atlanta','SanFrancisco','Phila']

    cost = {
        ('Cleveland','Dallas'): 8,
        ('Cleveland','Atlanta'): 6,
        ('Cleveland','SanFrancisco'): 10,
        ('Cleveland','Phila'): 9,
        ('Chicago','Dallas'): 9,
        ('Chicago','Atlanta'): 12,
        ('Chicago','SanFrancisco'): 13,
        ('Chicago','Phila'): 7,
        ('Boston','Dallas'): 14,
        ('Boston','Atlanta'): 9,
        ('Boston','SanFrancisco'): 16,
        ('Boston','Phila'): 5
    }

    supply = {
        ('Cleveland'):35,
        ('Chicago'):50,
        ('Boston'): 40
    }

    demand = {
        ('Dallas'): 45,
        ('Atlanta'): 20,
        ('SanFrancisco'): 30,
        ('Phila'): 30
    }

    # Create a new model
    m = Model("transport_problem_1")
    m.setParam( 'OutputFlag', False )
    # Create variables
    flow = {}
    for f in factories:
        for s in stores:
            flow[f,s] = m.addVar(obj=cost[f,s], name='flow_%s_%s' % (f, s))

    # Integrate new variables
    m.update()

    # Add supply constraints
    for f in factories:
        m.addConstr(quicksum(flow[f,s] for s in stores) == supply[f], 'supply_%s' % (f))
    
    # Add demand constraints
    for s in stores:
        m.addConstr(quicksum(flow[f,s] for f in factories) == demand[s], 'demand_%s' % (s))

    # Optimize the model. The default ModelSense is to is to minimize the objective, which is what we want.
    m.optimize()

    # Print solution
    if m.status == GRB.status.OPTIMAL:
        print ('\nOptimal flows :')
        for f in factories:
            for s in stores:
                print (f, '->', s, ':', flow[f,s].x)

except GurobiError:
    print ('Error reported')