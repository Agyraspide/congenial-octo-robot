from functools import reduce


def factorsSum(n):    
    return sum(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))-n
l = []
d = {}
for i in range(1,100001):
    if i < factorsSum(i):
        l.append(i)
        d[i] = 1

for _ in range(int(input())):
    n = int(input())
    i = 0
    foo = False
    while l[i]<n:
        if n-l[i] in d:
            foo = True
        i+=1
    print("YES") if foo else print("NO")