# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial
for _ in range(int(input())):
    print(sum(map(int, str(factorial(int(input()))))))