#!/bin/python3

import sys
def find(n):
    i=2
    ar=[]
    while(n>1):
        if n%i==0:
            ar.append(i)
            n=n//i
        else:
            i+=1
    return ar

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ar=[]
    arr=[]
    for i in range(2,n+1):
        ar=find(i)
        for j in ar:
            if ar.count(j)>arr.count(j):
                for q in range(ar.count(j)-arr.count(j)):
                    arr.append(j)
    net=1
    for i in arr:
        net=net*i
    print(net)
