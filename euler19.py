year = 1900
mon = {0: 'Jan', 1: 'Feb', 2:'Mar',3:'Apr', 4:'May', 5:'Jun', 6:'Jul', 7:'Aug',8:'Sep', 9:'Oct', 10:'Nov', 11:'Dec'}
days30 = ['Sep','Apr', 'Jun', 'Nov']
months = 0
day = 0
count = 0
while year<2001:
	m = mon[months%12]
	if m =='Feb' and ((year%4==0 and not year%100 ==0) or year%400==0):
		day+=29
	elif m=='Feb':
		day+=28
	elif m in days30:
		day+=30
	else:
		day+=31
	if day%7==6 and year>=1901:
		count+=1
	months+=1
	if months%12==0:
		year+=1
print(count)