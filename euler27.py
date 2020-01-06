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
def consecPrimes(i,j):
	count =0
	if i<0:
		i=-i
		for x in range(i+1):
			if (x**2-i*x+j) not in p:
				break
			count+=1
	for x in range(i+1):
		if (x**2+i*x+j) not in p:
			break
		count+=1
	return(count)
p= primes(2000000)
l = []
a = 0
while a <1001:
	if a in p:
		l.append(a)
	a+=1
max = 0
a = 0
b = 0
for j in l:
	for i in range(-j,j):
		if i%2==1 or i==2:
			if consecPrimes(i,j)> max:
				max = consecPrimes(i,j)
				a=i
				b=j
print(a)
print(b)
print(a*b)