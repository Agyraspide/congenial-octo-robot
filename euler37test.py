def primes(n):
    sieve = [True] * (n>>1)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i>>1]:
            sieve[i*i>>1::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n>>1) if sieve[i]]
	
l = {i:0 for i in primes(int(input()))}
s = 0
for i in l:
	if i<10:
		continue
	i = str(i)
	reduce = 1
	foo = True
	while len(i)>reduce:
		if int(i[reduce:]) not in l or int(i[:-reduce]) not in l:
			#print(i[reduce:])
			foo = False
			break
		reduce+=1
	if foo:
		s+=int(i)
print(s)
		