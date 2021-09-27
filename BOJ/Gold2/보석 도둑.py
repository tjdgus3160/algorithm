# 1202번
from heapq import heappop,heappush
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
arr=sorted([[*map(int,input().split())] for _ in range(n)])
bag=sorted([int(input()) for _ in range(k)])
res=0
i=0
hq=[]
for b in bag:
    while i<len(arr) and b>=arr[i][0]:
        heappush(hq,-arr[i][1])
        i+=1
    if hq:
        res+=-heappop(hq)
print(res)