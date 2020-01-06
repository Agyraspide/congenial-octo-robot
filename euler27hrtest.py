# Enter your code here. Read input from STDIN. Print output to STDOUT

def primes(n):
    sieve = [True] * (n>>1)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i>>1]:
            sieve[i*i>>1::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n>>1) if sieve[i]]
    
p = primes(2001)
def equations(n):
    l = []
    for i in p:
        if n%2==0:
            for j in range(-n+1,n-1,2):
                l.append([j,i])
        else:
            for j in range(-n,n,2):
                l.append([j,i])
    return l
def tester(l,n):
    tracker = 0
    mx = 0
    for i in range(len(l)):
        count = 0
        while (count**2+l[i][0]*count+l[i][1]) in p and l[i][0]<n and l[i][1]<n:
            count+=1
        if count>mx:
            mx = count
            tracker = i
    return(l[tracker])

l = equations(2001)
print(*tester(l,int(input())))