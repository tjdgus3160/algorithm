# 7662번
from heapq import heappush, heappop
from collections import defaultdict
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    maxhq = []
    minhq = []
    dic=defaultdict(int)
    s=set()
    for _ in range(int(input())):
        c,v=input().split()
        if c == "I":
            heappush(maxhq, -int(v))
            heappush(minhq, int(v))
            dic[int(v)]+=1
            s.add(int(v))
        else:
            if v=='1':
                while maxhq and dic[-1*maxhq[0]]==0:
                    heappop(maxhq)
                if maxhq:
                    k=-1*heappop(maxhq)
                    dic[k]-=1
                    if dic[k]==0:
                        s.remove(k)
            else:
                while minhq and dic[minhq[0]]==0:
                    heappop(minhq)
                if minhq:
                    k=heappop(minhq)
                    dic[k]-=1
                    if dic[k]==0:
                        s.remove(k)
    if s:
        print(max(s),min(s))
    else:
        print('EMPTY')
