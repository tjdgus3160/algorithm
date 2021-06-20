# 5046번
import sys
input=sys.stdin.readline

n,b,h,w=map(int,input().split())
res=float('inf')
flag=False
for _ in range(h):
    p=int(input())
    arr=[*map(int,input().split())]
    for a in arr:
        if a>=n and n*p<=b:
            res=min(res,n*p)
            flag=True
print(res if flag else 'stay home')