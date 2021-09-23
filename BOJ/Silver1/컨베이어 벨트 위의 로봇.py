# 20055번
from collections import deque
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
dq=deque([*map(int,input().split())])
arr=deque([False]*n)
res=1
while True:
    arr[-1]=False
    arr.rotate(1)
    dq.rotate(1)
    arr[-1]=False

    for i in range(n-2,-1,-1):
        if arr[i] and not arr[i+1] and dq[i+1]:
            arr[i],arr[i+1]=False,True
            dq[i+1]-=1

    if dq[0] and not arr[0]:
        dq[0]-=1
        arr[0]=True

    if dq.count(0)>=k:
        break
    res+=1
print(res)
