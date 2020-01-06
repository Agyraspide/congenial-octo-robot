#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = list(str(input().strip()))
    t =0
    s = num[:-k]
    for i in range(len(s)):
        a=1
        p = []
        for j in num[int(i):int(i)+k]:
            a = a*int(j)
        if a>t:
            t=a
    print(t)