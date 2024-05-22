n=input("Please input N for the Factorial: ")

fac=1
x=int(n)

while (x!=0):
	fac=fac*x
	x=x-1
    
print "The Factorial = "
print fac