#!/bin/python3
import timeit

import sys
fibs = {1:1,2:1}
def fib(n):
	if n in fibs:
		return(fibs[n])
	else:
		fibs[n] = fib(n-1) + fib(n-2)
		return(fibs[n])
   
t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	start = timeit.timeit()
	c = []
	i = 1
	while fib(i) < n:
		if fib(i)%2==0:
			c.append(fib(i))
		i+=1
	print(sum(c))
	print(start-timeit.timeit())