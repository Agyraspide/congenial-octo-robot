import inflect
p = inflect.engine()
l =[]
for i in range(1,1001):
	l.append(p.number_to_words(i).replace('-','').split())
t = 0
for i in range(len(l)):
	for j in range(len(l[i])):
		t+=len(l[i][j])
print(t)