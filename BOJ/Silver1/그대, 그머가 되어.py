# 14496번
import sys
import heapq
input=sys.stdin.readline
INF=sys.maxsize

def dijkstra(start):
    hq=[]
    res=[INF]*(n+1)
    res[start]=0
    heapq.heappush(hq,[0,start])
    while hq:
        dist,node=heapq.heappop(hq)
        for i in dic[node]:
            next=res[node]+1
            if next<res[i]:
                res[i]=next
                heapq.heappush(hq,[res[i],i])
    return res

a,b=map(int,input().split())
n,m=map(int,input().split())
dic={}
for i in range(1,n+1):
    dic.setdefault(i,[])
for _ in range(m):
    x,y=map(int,input().split())
    dic[x].append(y)
    dic[y].append(x)
dist=dijkstra(a)
print(dist[b] if dist[b] != INF else -1)
