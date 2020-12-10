# 1158번
from collections import deque
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
dq=deque([i for i in range(1,n+1)])
res=[]
t=1
while dq:
    tmp=dq.popleft()
    if t==k:
        res.append(tmp)
        t=1
        continue
    dq.append(tmp)
    t+=1
print("<"+", ".join(map(str,res))+">")