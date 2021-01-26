# 1021번
from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
dq=deque([*range(1,n+1)])
arr=[*map(int,input().split())]
res=0
for i in arr:
    if dq[0]==i:
        dq.popleft()
    elif dq.index(i)<=len(dq)//2:
        while dq[0]!=i:
            dq.append(dq.popleft())
            res+=1
        dq.popleft()
    elif dq.index(i)>len(dq)//2:
        while dq[0]!=i:
            dq.appendleft(dq.pop())
            res+=1
        dq.popleft()
print(res)