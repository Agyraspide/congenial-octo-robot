b = sorted(open('names.txt').read().rstrip().replace('"', '').split(','))
t = []
count = 0
for i in range(len(b)):
	for j in range(len(b[i])):
		count+=ord(b[i][j])-64
	t.append(count*(i+1))
	count=0
print(sum(t))