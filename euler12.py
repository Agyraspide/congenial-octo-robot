import sys
from math import ceil

def isprime(n):
	if n == 1:
		return False
	elif n % 2 == 0:
		return False
	for i in range(3, int(ceil(n ** 0.5)), 2):
		if n % i == 0:
			return False
	return True

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def p_fctr_exp(n):
    primes = prime_factors(n)
    exp=[]

    for p in primes:
        e=0
        while (n%p==0):
            n=n//p       # since p still divides n,
            e+=1         # we divide n by p and increase the exponent
        exp.append(e)
    return exp
def factor(n):
	a = 1
	for i in p_fctr_exp(n):
		if i != 0:
			a*=(i+1)
	return(a)
	
d = {}
	
def find(n):
	summ = 0
	for i in range(1, 842161320):
		summ +=i
		if isprime(i) and i >15:
			continue
		if i not in d:
			d[i] = factor(summ)
		if d[i] > n:
			return int(summ)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(find(n))
'''
n = 17907120
print(p_fctr_exp(n))
print(factor(n))
'''