#!/bin/python3

import sys

def primes(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]
'''
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for i in primes(int(n**0.5)):
        if n%i==0:
            n/=i
        while n%i==0:
            n/=i
        if n ==1:
            break
    if n ==1:
        print(i)
    else:
        print(int(n))

'''
import time
start = time.time()
print(sum(primes(10)))
print(time.time()-start)
