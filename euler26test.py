def makeCoprime(n):
	while n%2==0:
		n>>=1
	while n%5==0:
		n//=5
	return(n)
	
def getCycleLength(n):
	mv = 10%n
	cm = mv
	k =1
	while True:
		if cm ==1:
			return k
		cm = (cm*mv)%n
		k+=1
	
d = {0:-1, 1:0, 2:0}
mxLength= 0
mxCycleAt =1
for i in range(3, 10001):
	cP = makeCoprime(i)
	if cP!=1:
		n = getCycleLength(cP)
		if(n>mxLength):
			mxLength = n
			mxCycleAt =i
	d[i] = mxCycleAt
	
for _ in range(int(input())):
	print(d[int(input())])
