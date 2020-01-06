def isPalindrome(x):
	if str(x) == str(x)[::-1]:
		return True
	else: return False

numbers = []
for num in range(1000000):
	if isPalindrome(num) and isPalindrome("{0:b}".format(num)):
		numbers.append(num)
print(sum(numbers))