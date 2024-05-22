# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 18:10:22 2019

@author: User
"""

import matplotlib.pyplot as plt 
import numpy as np
from sympy import Symbol
from scipy.optimize import linprog

A=np.array([5,4])
B=np.array([[6,4],[1,2],[-1,1]])
E=np.array([24,6,1])
xbounds=(0,None)
ybounds=(0,2)
res=linprog(-A,B,E,bounds=(xbounds,ybounds))
print(res)

x=np.linspace(0,5)
y1=(24-6*x)/4
y2=(6-x)/2
y3=1+x
plt.figure(1)
plt.xlim(0,5)
plt.ylim(0,2)
plt.axis([0, 6, 0, 5]) 
plt.plot(x,y1,x,y2,x,y3)
plt.axhline(2,color='r')
plt.show
