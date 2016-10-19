#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    d = int(input().strip())
    a=d//3
    b=d//5
    c=d//15
    total=(3*a*(a+1))//2+(5*b*(b+1))//2-(15*c*(c+1))//2
    if d%5==0 or d%3==0:
        print(total-d)
    else:
        print(total)
