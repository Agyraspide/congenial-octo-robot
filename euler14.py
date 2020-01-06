# Enter your code here. Read input from STDIN. Print output to STDOUT
cache_limit = 5000001
d = [0] * cache_limit
d[1]=1
def collatz(n):
    if n < cache_limit and d[n - 1] != 0:
        return d[n-1]
    if n%2==0:
        #print("even, %i"%n)
        r = 1+ collatz(n>>1)
    else:
        #print("odd, %i"%n)
        r = 1 + collatz(3*n+1)
    if n< cache_limit:
        d[n-1]=r
    return r
f={}
a = 0
b = 0
for i in range(1, 5000000):
    a = collatz(i)
    if a>=b:
        f[i]=i
        b = a
    else:
        f[i]=f[i-1]



t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(f[n])