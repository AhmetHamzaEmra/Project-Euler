t=int(input().strip())
for q in range(t):
    m=int(input().strip())
    tot=1
    for i in range(1,m+1):
        tot*=i
    ar=list(str(tot))
    ar=map(int,ar)
    print(sum(ar))
