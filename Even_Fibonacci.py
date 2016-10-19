#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ar=[]
    ar.append(1)
    ar.append(1)
    num=ar[1]+ar[0]
    i=2
    arr=[]
    while(num<=n):
        
        ar.append(ar[i-1]+ar[i-2])
        if num%2==0:
            arr.append(num)
        num=ar[i-1]+ar[i-2]
        
        i+=1
    ar.remove(ar[len(ar)-1])
    print(sum(arr)-2)
