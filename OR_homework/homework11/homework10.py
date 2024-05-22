import math 
import numpy

def knapsackDP(C,W,V):
    # C is the capacity, which is a constant
    # W is the weight vector
    # V is the value vector

    # fill in the logic for Dynamic Programming here:
    # ...

    f_result = numpy.zeros(C+1)
    items = len(W)
    indexs = numpy.zeros((C+1, items))

    for i in range(items):
        num_c = int(math.floor(C/W[i])+1)
        f = numpy.zeros((C+1, num_c))
        for j in range(C+1):
            for k in range(num_c):
                if j-W[i]*k < 0 :
                    f[j][k] = -1
                else:
                    f[j][k] = f_result[j-W[i]*k] + k * V[i]

        for j in range(C+1):
            index = numpy.argmax(f[j, :])
            indexs[j][i] = index
            f_result[j] = f[j][index]

    print(f_result)
    #optf is the optimal objective value 
    #result stores the optimal combination of goods in knapsack
    optf = numpy.zeros 
    result = []

    index = numpy.argmax(f_result)
    optf = f_result[index]
    result.append(int(indexs[index][i]))
    for i in range(items-2, -1, -1):
        #print(index)
        #print("i:%d" % i)
        index = int(index - W[i+1] * indexs[index][i+1])
        result.insert(0, int(indexs[index][i]))
    print('objective value: ', optf)
    print('combinations are:', result)

knapsackDP(4, [2,3,1], [31,47,14])
knapsackDP(8, [3,8,5], [4,6,5])