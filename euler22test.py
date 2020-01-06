a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d = {}
for i in range(len(a)):
	d[a[i]] = i+1

def getScore(name, rank):
	foo = sum([d[i] for i in name])
	return rank*foo
	
l = []

for _ in range(int(input())):
	l.append(input())
l.sort()
answer = {}
for i in range(len(l)):
	answer[l[i]] = getScore(l[i],i+1)

for j in range(int(input())):
	print(answer[input()])