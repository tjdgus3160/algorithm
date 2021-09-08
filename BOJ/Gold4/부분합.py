# 1806번
import sys
input=sys.stdin.readline

n,s=map(int,input().split())
arr=[*map(int,input().split())]
res=float('inf')
start=0
cur=0
for i in range(n):
    cur+=arr[i]
    while cur>=s:
        cur-=arr[start]
        start+=1
    if i-start+2>0 and start:
        res=min(res,i-start+2)
print(res if res!=float('inf') else 0)
