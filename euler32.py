def checkPan(a,p):
	pNew = p[:]
	foo = True
	for i in a:
		if i not in pNew:
			foo=False
			break
		else:
			pNew.remove(i)
	if len(pNew)>0:
		foo = False
	return(foo)

a = '123456789'
l=[]
for i in a:
	l.append(i)
d = {}
x = []
for i in range(1,10000):
	for j in range(1,10000):
		k = i*j
		if k not in d:
			t = str(i)+str(j)+str(k)
			if len(t)<9:
				continue
			if checkPan(t,l):
				d[k] =i
				x.append(k)
	print(i)
print(sum(x))