#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum=0
    for i in range(n+1):
        sum+=i
    total=sum**2
    print(total-(n*(n+1)*((2*n)+1))//6)
