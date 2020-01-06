import time
import numpy
def primes(n):
	#finds all primes from 2 to n
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]
n = 3942396624067248157 #our coprime that we are cracking
start = time.time() #timer
p= primes(int(n**.5)+1) #creating numpy array of all primes from 2 to sqrt(n)+1
t1 = 0
t2= 0
for i in range(len(p)):
	if n%p[i]==0: 
		#brute force test to see if we have found the primes
		t1=p[i]
		t2=n//p[i]
		break
print("Prime one: %s Prime Two: %s Found in: %s" %(str(t1),str(t2),str(time.time()-start)))