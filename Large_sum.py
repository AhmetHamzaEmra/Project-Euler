n=int(input().strip())
sum=0
for i in range(n):
    b=int(input().strip())
    sum+=b
strn=str(sum)
for i in range(10):
    print(strn[i], end="")
