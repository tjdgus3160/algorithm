# 11000번
from heapq import heappush,heappushpop
import sys
input=sys.stdin.readline

room=set()
arr=sorted([[*map(int,input().split())]for _ in range(int(input()))])
hq=[]
res=0
for start,end in arr:
    if not hq:
        heappush(hq,end)
        res+=1
    else:
        if hq[0]<=start:
            heappushpop(hq,end)
        else:
            heappush(hq,end)
            res+=1
print(res)