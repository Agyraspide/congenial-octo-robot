#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	while n>0:
		n-=1
		if str(n) == str(n)[::-1]:
			for i in range(100,1000):
				if n%i==0:
					if len(str(n//i))==3:
						print(i,n//i)
						print(n)
						n =0
		