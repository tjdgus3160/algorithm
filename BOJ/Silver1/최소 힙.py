# 1927번
import heapq
import sys
input=sys.stdin.readline

hq=[]
for _ in range(int(input())):
    x=int(input())
    if x==0:
        if not hq:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq,x)