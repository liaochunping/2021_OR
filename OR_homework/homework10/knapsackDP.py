import math 
import numpy

def KnapsackDP(W, val, wt):
 
    # dp[i] is going to store maximum
    # value with knapsack capacity i.
    dp = [0 for i in range(W + 1)]
    n =len(val)
    # Fill dp[] using above recursive formula
    for i in range(W + 1):
        for j in range(n):
            if (wt[j] <= i):
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])
 
    return dp[W] 
 
# Driver program
val = [31,47,14]
wt = [2,3,1]
W = 4
print(KnapsackDP(W, val, wt))