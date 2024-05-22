
import math
import numpy

class KnapsackDPResult(object):
    def __init__(self, optf = 0, result  = 0):
        # instance variables
        # optimal objective value
        self.optf = optf
        # optimal combination of goods in knapsack
        self.result = result
    def knapsackDP(self,C,W,V):

        # C is the capacity, which is a constant
        # W is the weight vector
        # V is the value vector
        
        # fill in the logic for Dynamic Programming here:
        items = len(W)
        f = numpy.zeros((items + 1, C + 1))
        #function f(item i, capacity c)
        qu = numpy.zeros((2, C + 1, 1))
        qu = qu.tolist()
        #quantity qu(pre vs later, capacity c)
        seq = range(items)
        seq.reverse()


        for i in seq:
            
            for x in range(C + 1): 

                for m in range(int(math.floor(x/W[i])) + 1):
                    rest = x - W[i] * m
                    maxone = max(f[i + 1][rest] + V[i] * m, f[i + 1][x], f[i][x])
                    if f[i + 1][x] == maxone:
                        f[i][x] = f[i + 1][x]
                        qu[0][x] = [0] + qu[1][x]
                    elif f[i + 1][rest] + V[i] * m == maxone:
                        f[i][x] = f[i + 1][rest] + V[i] * m
                        qu[0][x] = [m] + qu[1][rest]

            for j in range(C + 1):
                qu[1][j] = []
                for k in range(len(qu[0][j])):
                    qu[1][j].append(qu[0][j][k])
                
              
        # optf is the optimal objective value
        # result stores the optimal combination of
        # goods in knapsack
        self.optf = max(f[0])
        maxone = f[0].tolist().index(self.optf)
        self.result = qu[0][maxone][:items]
        #return KnapsackDPResult(optf, result)
