def find_base(num,base):  #2
    quotient = num/base    #3
    remainder = num%base
    if quotient == 0:   #4
        return ""
    else:
        return find_base(int(quotient),base) + str(int(remainder))    #5
		
def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False
	
num, base = list(map(int,input().split()))
c = 0
for i in range(1,num):
	if isPalindrome(str(i)):
		if isPalindrome(find_base(i,base)):
			c+=i
			
print(c)