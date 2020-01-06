import math
import time

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(int(n / i))
    for divisor in reversed(large_divisors):
        yield divisor
		
n = 28124
p = []
d = {}
start = time.time()
for i in range(n):
	if (sum(list(divisorGenerator(i)))-i)>i:
		p.append(i)
		d[i] = i
sums = 1
for i in range(2,n):
	boo = True
	for j in p:
		if j < i:
			if (i-j) in d:
				boo = False
				break
		else: break
	if boo: sums+=i
print(sums)
print(time.time()-start)