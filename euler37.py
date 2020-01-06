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
	
p = numpy.matrix.tolist(primes(2000000))
l = []
i = 4
while len(l)<11:
	print(p[i])
	for j in range(len(str(p[i]))):
		foo = True
		try:
			if int(str(p[i])[:-j]) not in p:
				foo = False
				break
		except ValueError:
			continue
	if foo:
		for j in range(len(str(p[i]))):
			try:
				if int(str(p[i])[j+1:]) not in p:
					foo = False
					break
			except ValueError:
				continue
	if foo:
		l.append(p[i])
	i+=1
print(l)
print(sum(l))