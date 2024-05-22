import  pivot as pi

row = input("Please input how many constrains are there: ")
A = []
print "Please input the matrix A:"
for i in range(row + 1):
    temp = raw_input("")
    temp_int = [int(x) for x in temp.split(',')]
    A.append(temp_int)

temp = raw_input("Please input the list BV:")
BV = [int(x) for x in temp.split(',')]


(check, index) = pi.check(A)
while(not(check)):
    piindex = pi.findpivot(A, index)
    (A, BV) = pi.pivot(A, BV, piindex, index)
    (check, index) = pi.check(A)

pi.pprint(A)
print(BV)


