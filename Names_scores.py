def search(ar, x):
    for i in range(len(ar)):
        if ar[i]==x:
            return i

numofname=int(input().strip())
ar=[]

for i in range(numofname):
    ar.append(input())
ar=sorted(ar)
task=int(input().strip())
for j in range(task):
    m=input()
    a=search(ar, m)
    m=list(m)
    sum=0
    for i in m:
        sum+=ord(i)
    sum-=(64*len(m))
    print(sum*(a+1))
