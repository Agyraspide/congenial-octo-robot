'''import sys
#import timeit
d = {}
def fib(x):
	if x in d:
		return(d[x])
	else:
		d[x]=(1/(5**0.5)*((((1+(5**0.5))/2)**x)-(((1-(5**0.5))/2)**x)))
		return(d[x])
   
t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	#start = timeit.timeit()
	c = []
	i = 3
	r = int(fib(i))
	print(r)
	while r < n:
		if r%2==0:
			c.append(r)
		i+=3
		r = int(fib(i))
	print(sum(c))
	#end = timeit.timeit()
	#print(start-end)'''
import sys
d = {0:1, 1:1}
def fib(i):
    if i in d:
        return(d[i])
    else:
        d[i]= fib(i-1)+fib(i-2)
        return(d[i])

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    l = [fib(i) for i in range(n) if (fib(i)<n and fib(i)%2==0)]
    print(sum(l))