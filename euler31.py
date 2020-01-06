def getWays(n, c):
    dp = [1] + n*[0]
    for i in range(len(c)):
        for j in range(c[i],n+1): dp[j]+=dp[j-c[i]]
    return(dp[-1])

d = {0:1}
c = [1,2,5,10,20,50,100,200]
def store(n):
    if n in d:
        return d[n]
    else:
        d[n] = getWays(n,c)%(10**9+7)
        return d[n]
#for i in range(0,10**5,3): store(i)
for _ in range(int(input())):
	print(store(int(input())))