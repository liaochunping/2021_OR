
import numpy as np

def pivot(A, BV, r, c):
    A = np.array(A)
    A = A.astype(float)
    A[r,:] = A[r,:]/A[r,c]
    rows = len(A)
    for i in range(rows):
        if i != r:
           A[i,:] = A[i,:] - A[i,c]*A[r,:]
    BV[r-1] = c
    return A, BV

def pprint (A):
    for list in A:
        print"[",
        for llist in list:
                print ("%5.1f," % llist),
        print "]"

def check(A):
    ans = True
    for i in range(1, len(A[0])):
        if A[0][i] < 0:
            return (False, i)

    return (True, -1)

def findpivot(A, vindex):
    i = 1
    while A[i][vindex] == 0:
        i += 1
        if i >= len(A):
            return -1
    min = A[i][-1]*1.0/A[i][vindex]
    ans = i
    while i < len(A):
        if A[i][vindex] == 0:
            i += 1
        else:
            temp = A[i][-1]*1.0/A[i][vindex]
            if temp < min and temp >0:
                min = temp
                ans = i
            i += 1
    return ans