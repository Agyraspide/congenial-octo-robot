# Enter your code here. Read input from STDIN. Print output to STDOUT
factorial = {0:1}
def fact(n):
	if n in factorial:
		return factorial[n]
	else:
		factorial[n] = n*fact(n-1)
		return factorial[n]

#from itertools import permutations

def factoradic(n):
	l = []
	count = 0
	for i in reversed(range(13)):
		while n/fact(i)>1:
			n-=fact(i)
			count+=1
		l.append(count)
		count = 0
	return l
def convertFactoradic(n):
	a = list('abcdefghijklm')
	s = ''
	for i in n:
		s+=a[i]
		del a[i]
	return s
	

#l =sorted(list(permutations(a)))

for _ in range(int(input())):
	print(convertFactoradic(factoradic(int(input()))))