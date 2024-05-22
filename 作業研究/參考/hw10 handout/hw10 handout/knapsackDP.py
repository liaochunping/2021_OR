import math 
import numpy

def output(i):
    print("")
    if i.getAttr('status') != 2:
        print(i.getAttr('status'))
    else:
        for x in i.getVars():
            if x.x != 0:
                print ("%s: %f" % (x.varName, x.x))
        print('Obj: %f' % i.objVal)
def output_matrix(input):
    for i in range(len(input)):
        for j in range(len(input[0])):
            print(input[i][j]),
            print(", "),
        print("")
    print("")

class KnapsackDPResult(object): # save this in the KnapsackDP.py file
    def __init__(self, f, result):
        # instance variables
        self.f = f # optimal objective value
        self.result = result # optimal combination of goods in knapsack


def knapsackDP(C,W,V):
    # C is the capacity, which is a constant
    # W is the weight vector
    # V is the value vector

    # fill in the logic for Dynamic Programming here:
    # ...

    f_result = numpy.zeros(C+1)
    times = len(W)
    indexs = numpy.zeros((C+1, times))

    for i in range(times):
        num_c = int(math.floor(C*1.0/W[i])+1)
        f = numpy.zeros((C+1, num_c))
        for j in range(C+1):
            for k in range(num_c):
                if j-W[i]*k < 0 :
                    f[j][k] = -1
                else:
                    f[j][k] = f_result[j-W[i]*k] + k * V[i]
        #print(f)

        for j in range(C+1):
            index = numpy.argmax(f[j, :])
            indexs[j][i] = index
            f_result[j] = f[j][index]

    #print(indexs)

    
    #optf is the optimal objective value 
    #result stores the optimal combination of goods in knapsack
    optf = numpy.inf 
    result = []

    index = numpy.argmax(f_result)
    optf = f_result[index]
    result.append(int(indexs[index][i]))
    for i in range(times-2, -1, -1):
        #print(index)
        #print("i:%d" % i)
        index = int(index - W[i+1] * indexs[index][i+1])
        result.insert(0, int(indexs[index][i]))

    #print(index)
    return KnapsackDPResult(optf, result)    
             