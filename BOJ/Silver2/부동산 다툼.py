# 20364번
import sys
input=sys.stdin.readline

n,q=map(int,input().split())
arr=[0]*(n+1)
for _ in range(q):
    v=int(input())
    k=v
    bp=0
    flag=False
    while k>=1:
        if arr[k]:
            bp = k
            flag=True
        k//=2
    if k==0 and not flag:
        arr[v]=1
        print(0)
    else:
        print(bp)