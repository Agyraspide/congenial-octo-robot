# Enter your code here. Read input from STDIN. Print output to STDOUT
f = {0:1, 1:1}
def fib(x):
    if x in f:
        return f[x]
    else:
        f[x]= fib(x-1)+fib(x-2)
        return f[x]
def fibDigits(x):
    return(len(str(fib(x))))

d = {}

def findFibDigits(x):
    if fibDigits(x) in d:
        return d[fibDigits(x)]
    else:
        d[fibDigits(x)] = x
        return d[fibDigits(x)]
foo = 0
while findFibDigits(foo)<7000:
    #print(findFibDigits(foo))
    foo+=1
    '''
    if foo%1000==0:
        print(foo)'''
for _ in range(int(input())):
    n = int(input())
    while n not in d:
        n-=1
    print(d[n]+1)
    #print(fibDigits(7003))