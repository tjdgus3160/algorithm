# 3724번
import sys
input=sys.stdin.readline

res=[]
for _ in range(int(input())):
    m,n=map(int,input().split())
    tmp=[1]*m
    for _ in range(n):
        s=[*map(int,input().split())]
        for i in range(m):
            tmp[i]*=s[i]
    k=tmp[0]
    idx=1
    for i in range(1,m):
        if k<=tmp[i]:
            k=tmp[i]
            idx=i+1
    res.append(idx)
for i in res:
    print(i)