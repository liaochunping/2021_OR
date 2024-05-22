import numpy as np

def fibo2(n):
    fibo_list = [1, 1]
    i = 3
    if n >= 2:
        while i <= n:
            temp = fibo_list[i-2] + fibo_list[i-3]
            fibo_list.append(temp)
            i += 1
        print  fibo_list
    else:
        fibo_list = [1]
        print(fibo_list)