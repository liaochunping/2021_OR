# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 22:03:08 2019

@author: User
"""

from sympy import *
x = Symbol('x')
y = Symbol('y')
ans = solve([6*x+5*y-62,10*x+20*y-150],[x,y])
z=500*ans[x]+450*ans[y]
shadowprice=z-((5142*7+6)/7)
print"x1 =" ,ans[x],"x2 =",ans[y],"z =",z
print "shadowprice = " ,str(shadowprice)