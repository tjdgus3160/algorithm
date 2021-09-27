# 1715번
from heapq import heappop,heappush,heapify
import sys
input=sys.stdin.readline

hq=[int(input()) for _ in range(int(input()))]
heapify(hq)
res=0
if len(hq)==1:
    print(0)
    exit()
elif len(hq)<3:
    print(sum(hq))
    exit()
while hq:
    a=heappop(hq)
    if not hq:
        break
    b=heappop(hq)
    res+=a+b
    heappush(hq,a+b)
print(res)
