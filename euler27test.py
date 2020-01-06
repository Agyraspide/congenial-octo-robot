ab_pairs = set()
pos_primes = [2, ]

def primes_tester(x):
    mods = [abs(x) % d for d in range(2, (round(abs(x)**0.5) + 1))]
    if 0 not in mods:
        return True

for n in range(3, 1000, 2):
    if primes_tester(n):
        pos_primes.append(n)

neg_primes = [p * -1 for p in pos_primes]
primes = set(pos_primes + neg_primes)


for b in primes:
	for a in range(-1000, 1000):
		if (a%2!=0) or a==2:
			if abs(b + a + 1) < 1000:
				if (b + a + 1) in primes:
					ab_pairs.add((a, b))
			if abs(b + a + 1) >= 1000:
				if primes_tester((b + a + 1)):
					ab_pairs.add((a, b))

ab_pair_lst = list(ab_pairs)
n = 1
while len(ab_pairs) > 1:
    n += 1 # initalizing n at n=2
    ab_pair_lst = list(ab_pairs) # updating list to remove pairs removed from ab_pairs in previous iteration
    for (a, b) in ab_pair_lst:
        if abs(n**2 + (n * a) + b) < 1000:
            if (n**2 + (n * a) + b) not in primes:
                ab_pairs.discard((a, b))
        if abs(n ** 2 + (n * a) + b) >= 1000:
            if not primes_tester(n**2 + (n * a) + b):
                ab_pairs.discard((a, b))
print(ab_pairs)