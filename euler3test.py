#!/bin/python3

import sys

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n>>1)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i>>1]:
            sieve[i*i>>1::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n>>1) if sieve[i]]
'''
p = primes(10**6)
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    l = 2
    i = 0
    try:
        while n!=1:
            if n%p[i]==0:
                l = p[i]
                while n%p[i]==0:
                    n //= p[i]
            i+=1
        print(l)
    except:
        print(n)
'''
i = 10**6
p = primes(i)
#while len(primes(i))<10**5:
#	i+=1
print(len(p))