import sys
input=sys.stdin.readline

k=int(input())
res=[]
for i in range(int(input())):
    a,b=map(int,input().split())
    if a>b:
        if a-2>b+k-a:
            res.append(0)
        else:
            res.append(1)
    elif a<b:
        if b-1>a+k-b:
            res.append(0)
        else:
            res.append(1)
    else:
        res.append(1)
for i in res:
    print(i)
