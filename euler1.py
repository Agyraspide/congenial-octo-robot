import sys


t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	a = int((n-1)/3)
	b = int((n-1)/5)
	c = int((n-1)/15)
	print(int(3*((a*(a+1))>>1)+5*((b*(b+1))>>1)-15*((c*(c+1))>>1)))
	'''
print(4>>1)
'''