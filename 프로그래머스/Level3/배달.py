from collections import defaultdict
import heapq

def solution(N, road, K):
    dic=defaultdict(dict)
    for a,b,w in road:
        if b in dic[a]:
            dic[a][b]=min(dic[a][b],w)
        else:
            dic[a][b]=w
        if a in dic[b]:
            dic[b][a]=min(dic[b][a],w)
        else:
            dic[b][a]=w
    hq=[]
    res=[float('inf')]*(N+1)
    res[1]=0
    heapq.heappush(hq,[0,1])
    while hq:
        dist,node=heapq.heappop(hq)
        for i in dic[node]:
            next=res[node]+dic[node][i]
            if next<res[i]:
                res[i]=next
                heapq.heappush(hq,[res[i],i])
    # print(res)
    return len([1 for i in res if i<=K])