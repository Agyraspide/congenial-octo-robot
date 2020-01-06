'''
from fractions import Fraction as Fr
 
def bernoulli(n):
    A = [0] * (n+1)
    for m in range(n+1):
        A[m] = Fr(1, m+1)
        for j in range(m, 0, -1):
          A[j-1] = j*(A[j-1] - A[j])
    return A[0] # (which is Bn)

f = {0:1}
def factorial(n):
	if n in f:
		return f[n]
	else:
		f[n] = n*factorial(n-1)
		return f[n]
		
def binomial(n,k):
	return(factorial(n)/(factorial(k)*factorial(n-k)))
	
def sum(n,p):
	s = 0
	for j in range(p):
		s+= binomial(p+1,j)*bernoulli(j)*n**(p-j+1)
	return s/(p+1)
'''

def sum(n,p):
	return((n**(p+1)-1)/(n-1))
	
print(sum(5,5)-sum(5,1))
