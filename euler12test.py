# Enter your code here. Read input from STDIN. Print output to STDOUT
def divisors(n):
    a = 0
    t = 1
    for i in range (2, int(n ** 0.5) + 1):
        while n%i==0:
            a+=1
            n//=i
        t*=(a+1)
        a=0
    if n!=1:
        t*=2
    return(t)


def num(n):
    return((n*(n+1))>>1)
d={}
temp = 0
inc = 0
for i in range(1,501):
    while(temp<=i):
        inc+=1
        temp = divisors(num(inc))
    d[i]= num(inc)


        
for a0 in range(int(input())):
    n = int(input().strip())
    print(d[n])