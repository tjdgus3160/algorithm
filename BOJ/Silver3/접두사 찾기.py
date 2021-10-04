# 14426번
from bisect import bisect_left
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=sorted([input().rstrip() for _ in range(n)])
res=0
for _ in range(m):
    v=input().rstrip()
    k=bisect_left(arr,v)
    if k<n and len(arr[k])>=len(v) and arr[k][:len(v)]==v:
        res+=1
print(res)