#Fibonacci Number
def Fibonacci_Number(x):
    if x.isdigit() :
        f1 ,f2 = 1 ,1
        list = [f1,f2]
        for i in range(1 , int(x)-1):
            num = f1 +f2
            f1 = f2
            f2 = num
            list.append(num)
        print('The Fibonacci sequence = ')
        for i in range(0, int(x)):
            print(list[i] , end = ' ')
    else:
        print('this is not an integer')
#################################################################    
x =input('Please input the term n for the Fibonacci sequence: ')   
Fibonacci_Number(x)