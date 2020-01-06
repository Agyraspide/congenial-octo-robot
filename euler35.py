from math import sqrt

def rotate(n):
    n=str(n)
    return n[1:]+n[:1]
	
def isRotatable(n, p):
    for x in range(2,n):
        n = rotate(n)
        if not p[int(n)]:
            return False
    return True


def sieve(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    for x in range(4,n+1,2):
        primes[x] = False

    for x in range(3,int(sqrt(n))+1,2):
        if(primes[x]):
            for y in range(x*x,n+1,x):
                primes[y] = False

    return primes
count = 0
primes = sieve(1000000)
for x in range(2, len(primes)):
	if(isRotatable(x,primes)):
		count+=1
print(count)