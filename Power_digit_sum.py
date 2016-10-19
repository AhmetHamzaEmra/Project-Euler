t=int(input().strip())
for q in range(t):
    m=int(input().strip())
    a=2**m
    ar=list(str(a))
    ar=map(int,ar)
    print(sum(ar))
