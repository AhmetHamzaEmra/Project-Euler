#!/bin/python3

import sys

def IsPrime(n):
    if n==2:
        return True
    if n==1 or n%2==0:
        return False
    else:
        i=3
        while i*i<=n:
            if n%i==0:
                return False
                break
            i+=2
    return True

t = int(input().strip())
ar=[]
primes=[2]
for a0 in range(t):
    n = int(input().strip())
    ar.append(n)    
k=3
while (primes[len(primes)-1]<max(ar)):
    if IsPrime(k):
        primes.append(k)
    k+=2
#print(primes)
sum=0
for i in ar:
    sum=0
    for j in primes:
        if i>=j:
            sum+=j
        else:
            break
    print(sum)
    
