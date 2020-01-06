from itertools import permutations
a = '123456789'
n = int(input())
d = {''.join(i):0 for i in list(permutations(a[:n]))}
t = []
for i in range(100):
	for j in range(2000):
		foo = str(i)+str(j)+str(i*j)
		if foo in d:
			t.append(i*j)
#print(set(t))
print(sum(set(t)))
		