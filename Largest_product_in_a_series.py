#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    num=list(str(num))
    max=1
    for i in range(len(num)-k):
        asd=1
        for j in range(i,i+k):
            asd*=int(num[j])
        if asd>max:
            max=asd
    if max!=1:
        print(max)
    else:
        print("0")
