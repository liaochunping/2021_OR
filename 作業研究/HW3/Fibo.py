# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:10:56 2019

@author: User
"""

n = input('Please input the term n for the Fibonacci sequence: ')
i=1
j=1
print 'The Fibonacci sequence = '

while n >=1 :
    print str(j),
    i,j=j+i,i
    n-= 1
    