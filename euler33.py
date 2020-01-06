def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
    while b:
        a, b = b, a % b
    return a
def simplify_fraction(numer, denom):

    if denom == 0:
        return "Division by 0 - result undefined"

    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    # Note that reduced_den > 0 as documented in the gcd function.

    if reduced_den == 1:
        return (reduced_num, reduced_den)
    elif common_divisor == 1:
        return (numer, denom)
    else:
        return (reduced_num, reduced_den)
		

x = '123456789'
goal = []
for i in range(1,101):
	for j in range(1,101):
		for k in x:
			t1 = str(i)
			t2 = str(j)
			
			if k not in t1:
				continue
			else:
				t1 = t1.replace(k,'')
			if k not in t2:
				continue
			else:
				t2 = t2.replace(k,'')
			if len(t1) == 0 or len(t2) ==0:
				continue
			f = (t1,t2)
			if simplify_fraction(int(t1),int(t2)) == simplify_fraction(i,j) and int(t1)/int(t2)<1:
				goal.append(f)
print(goal)
