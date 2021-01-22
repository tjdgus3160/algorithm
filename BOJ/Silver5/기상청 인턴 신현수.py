# 2435번
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
arr=[*map(int,input().split())]

res=None
for i in range(n-k+1):
    tmp=0
    for j in range(k):
        tmp+=arr[i+j]
    if res==None:
        res=tmp
    res=max(res,tmp)
print(res)