ones = ("", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
tens = ("", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
teens = ("ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")

def word(w):
	if w>=10**12:
		a = w//(10**12)
		return(word(a) + "Trillion " + word(w-(a*(10**12))))
	elif w>=10**9:
		a = w//(10**9)
		return(word(a) + "Billion " + word(w-(a*(10**9))))
	elif w>=10**6:
		a = w//(10**6)
		return(word(a) + "Million " + word(w-(a*(10**6))))
	elif w>=10**3:
		a = w//(10**3)
		return(word(a) + "Thousand " + word(w-(a*(10**3))))
	elif w>=100:
		a = w//100
		return(word(a) + "Hundred " + word(w-(a*100)))
	elif w>=10:
		if w>20:
			a = w//10
			return(tens[w//10]+ ' ' + word(w-(a*10)))
		else:
			return(teens[w%10]+ ' ')
	else:
		if w>0:
			return(ones[w]+ ' ')
		else:
			return('')

print(word(104382426112).title())