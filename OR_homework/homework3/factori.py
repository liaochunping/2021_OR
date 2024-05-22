def factorial(x):
    if x.isdigit() :
        fact = 1
        for i in range(1 , int(x)+1):
            fact = fact * i
        print('The Factorial =')
        print(fact)
    else:
        print('this is not an integer')
        
###################################################
x =input('Please input N for the Factorial: ')
factorial(x)