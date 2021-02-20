# 17484번
from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[]
res=float('inf')
for _ in range(n):
    arr.append([*map(int,input().split())])
dq=deque()
for i in range(m):
    dq.append([1,i,arr[0][i],None])
while dq:
    k,x,v,d=dq.popleft()
    if k==n:
        res=min(res,v)
        continue
    for i in range(-1,2):
        if d!=i and 0<=x+i<m:
            dq.append([k+1,x+i,v+arr[k][x+i],i])
print(res)
