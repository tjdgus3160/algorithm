# 1697번
import sys
from _collections import deque
input=sys.stdin.readline

def func(n,k):
    q=deque()
    q.append((n,0))
    visited=[False]*(100001)
    visited[n]=True
    while q:
        loc,t=q.popleft()
        if loc==k:
            return t
        for i in [loc-1,loc+1,2*loc]:
            if 0<=i<=100000 and not visited[i]:
                visited[i]=True
                q.append((i,t+1))

n,k=map(int,input().split())
print(func(n,k))