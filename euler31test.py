c = [1,2,5,10,20,50,100,200]
d = {0:1}
def keymeasure(key):
    return d[key] and key

def count(n): 
	if n in d: 
		return d[n]
	dp = [1] + n*[0]
	for i in range(len(c)):
		for j in range(c[i],n+1): 
			dp[j]+=dp[j-c[i]]
	for i in range(max(d, key=keymeasure),len(dp)):
		d[i] = dp[i]%(10**9+7)
	return d[n]

for _ in range(int(input())):
	print(count(int(input())))
	