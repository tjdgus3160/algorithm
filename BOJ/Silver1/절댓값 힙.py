# 11286번
import heapq
import sys
input=sys.stdin.readline

hq=[]
dic={}
for _ in range(int(input())):
    x=int(input())
    if x==0:
        if not hq:
            print(0)
        else:
            k=heapq.heappop(hq)
            if -k in dic and dic[-k]>0:
                print(-k)
                dic[-k]-=1
            else:
                print(k)
    else:
        heapq.heappush(hq,abs(x))
        if x<0:
            dic.setdefault(x,0)
            dic[x]+=1