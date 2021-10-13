# 1655번
from heapq import heappush,heappop
import sys
input=sys.stdin.readline

maxhq=[]
minhq=[]
for _ in range(int(input())):
    n=int(input())
    if len(maxhq)==len(minhq):
        heappush(maxhq, -n)
    else:
        heappush(minhq,n)

    if maxhq and minhq and -maxhq[0]>minhq[0]:
        tmp_max=-heappop(maxhq)
        tmp_min=heappop(minhq)

        heappush(maxhq,tmp_max)
        heappush(minhq,tmp_min)
    print(-maxhq[0])