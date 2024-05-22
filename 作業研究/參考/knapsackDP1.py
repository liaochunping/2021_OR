import math
import numpy as np
class KnapsackDPResult(object):
    def __init__(self, f, result):
        # instance variables
        # optimal objective value
        self.f = f
        # optimal combination of goods in knapsack
        self.result = result
def knapsackDP(C,W,V):
    # C is the capacity, which is a constant
    # W is the weight vector
    # V is the value vector
    # fill in the logic for Dynamic Programming here:
    s = np.zeros((len(W)+1,C+1))
    combination=np.zeros((C+1))
    for n in range(1,len(W)+1):
    	for i in range(0,C+1):
    		x=math.floor(i/W[n-1])
    		if(x>0):
    			if(x*V[n-1]+s[n-1,i-x*W[n-1]]>s[n-1,i]):
    				s[n,i]=x*V[n-1]+s[n-1,i-x*W[n-1]]
    				combination[i]=n
    			else:
    				s[n,i]=s[n-1,i]
    		else:
    			s[n,i]=s[n-1,i]
    res=np.zeros((len(W)))
    res[int(combination[C])-1]=1
    weight=C-W[int(combination[C])-1]
    while (combination[weight]>0):
    	res[int(combination[weight])-1]=res[int(combination[weight])-1]+1
    	weight=weight-W[int(combination[weight])-1]
    # optf is the optimal objective value
    # result stores the optimal combination of
    # goods in knapsack
    optf = s[len(W),C]
    result = res
    return KnapsackDPResult(optf, result)