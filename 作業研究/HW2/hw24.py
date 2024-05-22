
x=[]
times = 50
print "integers from 1 to 50 divisible by 11 : " ,
for i in range(1,times):
    if(i % 11 == 0):
        x.append(i)
        print x,
        
times=31
#從0開始 所以要設31
x=[]

for i in range(1,times):
	if(i%5==0 or i%7==0):
		x.append(i)
print"integers from 1 to 30 divisible by 5 or 7 : ",x

x=[]

for i in range(1,times):
	if(i%2==0 and i%7==0):
		x.append(i)
print"integers from 1 to 30 divisible by 2 and 7 : ",x

count=1
x=[]
while (count<=20):
	if(count%2!=0 and count%7!=0):
		x.append(count)
	count = count+1
    
print"integers from 1 to 20 not divisible by 2 nor 7 : ",x

count=1
x=[]
while (count<=20):
	if(count%2!=0):
		x.append(count)
	count = count+1
    
print"odd integers from 1 to 20 : ",x


