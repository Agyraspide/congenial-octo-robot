def pythagoreanTriplets(limits) : 
	c, m = 0, 2
	l = []
	# Limiting c would limit  
	# all a, b and c 
	while c < limits : 
		
		# Now loop on n from 1 to m-1 
		for n in range(1, m) : 
			a = m * m - n * n 
			b = 2 * m * n 
			c = m * m + n * n 
			# if c is greater than 
			# limit then break it 
			if c > limits : 
				break
			l.append([a, b, c]) 
  
		m = m + 1
	return(sorted(l,key = sum))	
		
print(pythagoreanTriplets(100))	