#!/bin/python3

import sys
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n>>1)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i>>1]:
            sieve[i*i>>1::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n>>1) if sieve[i]]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    p = primes(n+1)
    a = 1
    for i in p:
        for j in range(2,6):
            if i**j<n:
                a*=i
        a*=i
    print(a)

