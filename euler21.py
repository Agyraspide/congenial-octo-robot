from functools import reduce

def factorsSum(n):    
    return sum(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))-n
             
d = {}
f = {}
for i in range(1,2*10**5):
    d[i] = factorsSum(i)

def answer(n):
    if n in f:
        return(f[n])
    else:
        l = []
        for key in range(1,n):
            if d[key] in d and key!=d[key] and key ==d[d[key]]:
                l.append(key)
        
        if len(l)>=2:
            for i in range(1,len(l)):
                for j in range(l[i-1],l[i]):
                    f[j] = sum(l[:i])
        for i in range(l[-1],n+1):
            
            f[i] = sum(l)
        return(f[n])
        
    
for _ in range(int(input())):
    print(answer(int(input())))