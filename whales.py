# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 12:00:41 2017

@author: Brandon
"""
import matplotlib.pyplot as plt
global bCap,fCap, bMin, fMin, bGrowth, fGrowth
bCap = 150000
fCap = 400000
bMin=3000
fMin=15000
bGrowth= .05
fGrowth=.08

def blueDelta(x,y,a):
    return(int(bGrowth*x*((x-bMin)/(x+bMin))*(1-x/bCap)-a*x*y))
def finDelta(x,y,a):
    return(int(fGrowth*y*((y-fMin)/(y+fMin))*(1-y/fCap)-a*x*y))

bStart = 5000
fStart= 70000
bPop = bStart
fPop = fStart
alpha = 10**-8
equil = []
shutoff =0

bTotal = [bPop]
fTotal = [fPop]
for i in range(5):
    for x in range(2500):
            bCopy = bPop
            bPop = bPop+blueDelta(bPop,fPop,alpha)
            fPop = fPop+finDelta(bCopy,fPop,alpha)
            bTotal.append(bPop)
            fTotal.append(fPop)
            if bPop >= 137698 and fPop >= 392568:
                if shutoff == 1:
                    continue
                equil.append([x+2,fMin])
                shutoff =1
    plt.plot(bTotal,label = "Blue Minimum Population: " + str(bMin))
    plt.plot(fTotal, label = "Fin Minimum Population: " + str(fMin))
    fMin+=1000
    
    bTotal = [bStart]
    fTotal = [fStart]
    bPop = bStart
    fPop = fStart
    shutoff =0
    
alpha =10**-8

plt.xlabel("Years")
plt.ylabel("Whale Population")
plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
plt.show()
print(equil)