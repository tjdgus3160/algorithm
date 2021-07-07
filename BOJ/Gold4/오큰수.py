# 17298번
from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
res=[-1]*(n)
arr=[*map(int,input().split())]

dq=deque([arr[-1]])
for i in range(n-2,-1,-1):
    while dq and dq[-1]<=arr[i]:
        dq.pop()
    if dq:
        res[i]=dq[-1]
    dq.append(arr[i])
print(*res)