from functools import reduce



foo = [220,284,1184,1210,2620,2924,5020,5564,6232,6368,10744, 10856,12285,14595,17296,18416,63020,66928,66992,67095, 69615,71145,76084,79750,87633,88730]

for _ in range(int(input())):
	n = int(input())
	answer = 0
	for i in foo:
		print(i)
		if i<n:
			answer+=i
		else:
			break
	print(answer)