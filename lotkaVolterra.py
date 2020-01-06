# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 14:00:03 2017

@author: Brandon
"""
from pylab import *


x =1000.
y =40.

dt = .0000001

a = 0.04
b = 0.0005
c = 0.2
d = 0.01
xlist = [x]
ylist = [y]

for i in range(500000):
    xcopy = x
    
    x = x+ ((a*x*(1-x)-b*x*y)*dt)
    y = y+((-c*y+d*xcopy*y)*dt)
    
    xlist.append(x)
    ylist.append(y)
    
plot(xlist)
plot(ylist)