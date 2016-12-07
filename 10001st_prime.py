#!/bin/python3

import sys

def IsPrime(n):
    
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

i=3
while len(primes)<max(ar):
    if IsPrime(i):
        primes.append(i)
    i+=2
for k in range(len(ar)):
    
    print(primes[ar[k]-1])
