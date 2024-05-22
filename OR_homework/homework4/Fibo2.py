#Fibonacci Number
def fibo2(x):
    if x ==1:
        list =[1]
        print(list)
    else :
        f1 ,f2 = 1 ,1
        list = [f1,f2]
        for i in range(1 , int(x)-1):
            num = f1 +f2
            f1 = f2
            f2 = num
            list.append(num)
        print(list)
