#!/bin/python3

import sys

def primes(n):
    sieve = [True] * (n>>1)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i>>1]:
            sieve[i*i>>1::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n>>1) if sieve[i]]
p = primes(10**6)
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(p[n-1])

