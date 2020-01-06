n = 31192087
cave = [i for i in range(n)]
print(cave)
i =0
while len(cave)>2:
	while i< len(cave):
		cave.pop(i)
		#print(cave)
		i+=2
	i-=len(cave)
print(cave)

def find_ternary(num):  #2
    quotient = num/3    #3
    remainder = num%3
    if quotient == 0:   #4
        return ""
    else:
        return find_ternary(int(quotient)) + str(int(remainder))    #5


print(find_ternary(31))
print(find_ternary(19))
print(find_ternary(29))