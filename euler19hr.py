for _ in range(int(input())):
	y1, m1, d1 = input().split()
	y2, m2, d2 = input().split()
	y1, m1, d1 = int(y1), int(m1), int(d1)
	y2, m2, d2 = int(y2), int(m2), int(d2)
	year = 1900
	mon = {0: 'Jan', 1: 'Feb', 2:'Mar',3:'Apr', 4:'May', 5:'Jun', 6:'Jul', 7:'Aug',8:'Sep', 9:'Oct', 10:'Nov', 11:'Dec'}
	days30 = {'Sep':0,'Apr':0, 'Jun':0, 'Nov':0}
	months = 0
	day = 1
	count = 0
	tot_days = 1
	
	while (year<=y2):
		if year == y2 and mon == m2-1 and day == d2:
			break
		m = mon[months%12]
		if m =='Feb' and ((year%4==0 and not year%100 ==0) or year%400==0):
			if day==30:
				months+=1
				day =1
		elif m=='Feb':
			if day==29:
				months+=1
				day =1
		elif m in days30:
			if day==31:
				months+=1
				day =1
		else:
			if day==32:
				months+=1
				if months%12==0:
					year+=1
				day =1
		#if tot_days%7==0:
			#print(str(day) + ' ' + m + ' ' + str(year))
		if tot_days%7==0 and year>=y1 and day ==1:
			if year == y1:
				if months < m1:
					day+=1
					tot_days+=1
					continue
				else:
					if day < d1:
						day+=1
						tot_days+=1
						continue
			#print(str(day) + ' ' + m + ' ' + str(year))
			count+=1
		day+=1
		tot_days+=1
	print(count-2)