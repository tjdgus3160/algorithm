# 11279번
from heapq import heappop, heappush
import sys
input=sys.stdin.readline

hq=[]
for _ in range(int(input())):
    x=int(input())
    if x:
        heappush(hq,-x)
    else:
        if not hq:
            print(0)
        else:
            print(-1*heappop(hq))