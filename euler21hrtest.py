from math import floor

def zeller(day, month, year) : 
    if (month == 1) : 
        month = 13
        year = year - 1
  
    if (month == 2) : 
        month = 14
        year = year - 1
    q = day 
    m = month 
    k = year % 100; 
    j = year // 100; 
    h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j 
    h = h % 7
    return h 
	
#print(zeller(30, 12, 19, floor(2019/100)))

for _ in range(int(input())):
	y1, m1, d1 = list(map(int,input().split()))
	y2, m2, d2 = list(map(int,input().split()))
	count = 0
	for i in range(y1, y2+1):
		for j in range (1, 13):
			if (i==y1 and j<m1) or (i==y1 and j==m1 and d1!=1):
				continue
			elif (i==y2 and j>m2):
				break
			else:
				if zeller(1, j, i)==1:
					count+=1
					#print(j, i)
	print(count)