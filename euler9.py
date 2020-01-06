t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    l = -1
    for a in range(n//3+1):
        b = int((n**2-2*n*a)/(2*(n-a)))
        c = n-a-b
        if c**2 == a**2+b**2:
            temp = a*b*c
            if temp>l:
                l = temp
    print(l if l>0 else '-1')



