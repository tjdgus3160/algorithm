# 15903번
from heapq import heapify,heappop,heappush
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
hq=[*map(int,input().split())]
heapify(hq)
for _ in range(m):
    a=heappop(hq)
    b=heappop(hq)
    heappush(hq,a+b)
    heappush(hq,a+b)
print(sum(hq))