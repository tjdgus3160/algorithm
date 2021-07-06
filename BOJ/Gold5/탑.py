# 2493번
from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
arr=[*map(int,input().split())]
res=[0]*n
dq=deque([[1,arr[0]]])
for i in range(1,n):
    while dq and dq[-1][1]<arr[i]:
        dq.pop()
    if dq:
        res[i]=dq[-1][0]
    dq.append([i+1,arr[i]])
print(*res)