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
"""
用dual function 檢查答案Z是否等於20 dual function計算過程放在pdf第二頁中
"""
A = [[-1, -10, -6, -15, 0, 0, 0, 0], [0, 1, 1, 3, 1, 0, 0, 2], [0, -1, -2, -4, 0, 1, 0, 3], [0, 1, 3, 5, 0, 0, 1, 4]]
BV = [4,5,6]
print(A)
print(BV)
A1 ,B1 =pivot(A,BV ,1 ,3)
print(A1)
print(B1)
A2 ,B2 = pivot(A1 , B1 ,1 ,1)
print(A2)
print(B2)