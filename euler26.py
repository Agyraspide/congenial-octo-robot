def convert(numerator, denominator):
    #print("---->", numerator, "/", denominator)
    result = [str(numerator//denominator) + "."]
    subresults = [numerator % denominator]          ### changed ###
    numerator %= denominator
    while numerator != 0:
        #print(numerator)
        numerator *= 10
        result_digit, numerator = divmod(numerator, denominator)
        result.append(str(result_digit))             ### moved before if-statement

        if numerator not in subresults:
            subresults.append(numerator)
            #print("appended", result_digit)

        else:
            result.insert(subresults.index(numerator) + 1, "(")   ### added '+ 1'
            #print("index", subresults.index(numerator), subresults, "result", result)
            result.append(")")
            #print("repeating", numerator)
            break
    #print(result)
    return "".join(result)
max = 0
answer = 0
for i in range(1,1001):
	a = convert(1,i)
	if len(a)>max:
		max = len(a)
		answer = i
print(answer)