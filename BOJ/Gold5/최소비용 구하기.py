# 1916번
from collections import defaultdict
import heapq
import sys
input=sys.stdin.readline
INF=sys.maxsize

def func(start):
    global n
    hq=[]
    res=[INF]*(n+1)
    res[start]=0
    heapq.heappush(hq,[0,start])
    while hq:
        dist,node=heapq.heappop(hq)
        for i in range(1,n+1):
            if i in dic[node]:
                next=res[node]+dic[node][i]
                if next<res[i]:
                    res[i]=next
                    heapq.heappush(hq,[res[i],i])
    return res

n=int(input())
dic=defaultdict(dict)
for _ in range(int(input())):
    a,b,w=map(int,input().split())
    if b not in dic[a] or dic[a][b]>w:
        dic[a][b]=w
start,end=map(int,input().split())
res=func(start)
print(res[end])