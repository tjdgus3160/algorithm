# 13549번
from heapq import heappush,heappop
import sys
input=sys.stdin.readline

def func(n,k):
    hq = []
    heappush(hq, (0, n))
    visited=[False]*(100001)
    visited[n]=True
    while hq:
        t, loc = heappop(hq)
        if loc==k:
            return t
        for i in [loc-1,loc+1,loc*2]:
            if 0<=i<=100000 and not visited[i]:
                visited[i]=True
                if i==loc*2:
                    heappush(hq,(t, i))
                else:
                    heappush(hq,(t + 1,i))

n,k=map(int,input().split())
print(func(n,k))
