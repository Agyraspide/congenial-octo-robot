# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:30:14 2017

@author: Brandon
"""

def f1(x1, x2, a, q, e):
    return(.05*(1-x1/150000)-a*x1*x2-q*e*x1)
def f2(x1,x2,a,q,e):
    return(.08*(1-x2/400000)-a*x1*x2-q*e*x2)
    
a= 10^(-8)
q = 10^(-5)

x1 = 150000
x2 = 400000
for e in range(50000):
    for t in range(500):
        tempx1 = x1
        tempx2 = x2
        x1 = f1(tempx1, tempx2, a,q, e)
        x2= f2(tempx1,tempx2,a,q,e)
    if (x1 == 0) or (x2 ==0):
        break
        
print(e)