# 2075번
from heapq import heappush,heappop
import sys
input=sys.stdin.readline

hq=[]
n=int(input())
for _ in range(n):
    for i in [*map(int,input().split())]:
        if not hq or hq[0]<i:
            if len(hq)==n:
                heappop(hq)
            heappush(hq,i)
print(hq[0])
