import math
x = math.factorial(9)*7
l = []

for i in range(3,x):
	b = 0
	a = str(i)
	for j in a:
		b+=math.factorial(int(j))
	if b ==i:
		l.append(b)
print(sum(l))