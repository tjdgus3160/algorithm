# 1753번
import sys
import heapq
INF=sys.maxsize

def dijkstra(k):
    n=len(graph)
    v=[]
    d=[INF]*n
    heapq.heappush(v,[0,k])
    while v:
        tmpv,tmpi=heapq.heappop(v)
        if d[tmpi]<tmpv:
            continue
        else:
            d[tmpi]=tmpv
        for i in graph[tmpi].keys():
            next=tmpv+graph[tmpi][i]
            if next<d[i]:
                d[i]=next
                heapq.heappush(v,[d[i],i])
    return d[1:]

V,E=map(int,input().split())
k=int(input())
graph=[{} for _ in range(V+1)]
for _ in range(E):
    u,v,w=map(int,sys.stdin.readline().split())
    if v in graph[u]:
        graph[u][v] = min(graph[u][v],w)
    else:
        graph[u][v]=w
result=dijkstra(k)
for i in result:
    sys.stdout.writelines("{}\n".format(i) if i != INF else "INF\n")