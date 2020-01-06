foo = 10**9+7
for _ in range(int(input())):
    n = int(input())
    m = (n - 1)//2
    result  = 4*((m*n*n) - (((m - 1)*m*16)>>1) - ((8*m*(m - 1)*(m - 2))//3)) - (6*((n - 1)*(n + 1)>>2)) + 1
    print(int(result%foo))