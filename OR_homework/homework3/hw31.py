def divisible_by_11_from1to50():
    print('integers from 1 to 50 divisible by 11 : ',end = '')
    for i in range (1 ,51 ):
        if (i%11 ==0) :
            print(i,end = ' ')
def divisible_by_5or7_from1to30():
    print('integers from 1 to 30 divisible by 5 or 7 : ',end = '')
    for i in range (1 ,31 ):
       if (i%5 ==0 )or (i%7==0):
           print(i,end = ' ')
def divisible_by_2and7_from1to30():
    print('integers from 1 to 30 divisible by 2 and 7 : ',end = '')
    for i in range (1 ,31 ):
       if (i%2 ==0 )and (i%7==0):
           print(i,end = ' ')            
def notdivisible_by_2nor7_from1to20():     
    print('integers from 1 to 20 not divisible by 2 nor 7 : ',end = '')
    i = 1
    while i < 21 :
        if (i%2 != 0 ) and (i%7 != 0):
             print(i,end = ' ')
        i = i+1
def oddintegers_from_1to20():
    print('odd integers from 1 to 20 : ',end = '')
    i = 1
    while i < 21 :
        if (i%2 == 0):
            print(i,end = ' ')
        i = i+1
##################################################################
divisible_by_11_from1to50()
print('')
divisible_by_5or7_from1to30()
print('')
divisible_by_2and7_from1to30()
print('')
notdivisible_by_2nor7_from1to20()
print('')
oddintegers_from_1to20()