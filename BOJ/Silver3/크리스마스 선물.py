# 14235번
from heapq import heappop,heappush
import sys
input=sys.stdin.readline

hq=[]
for _ in range(int(input())):
    s=input().rstrip()
    if s=='0':
        print(-1*heappop(hq) if hq else -1)
    else:
        for i in [*map(int,s.split())][1:]:
            heappush(hq,-1*i)