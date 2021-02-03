import sys
INF=sys.maxsize
import heapq
def dijkstra(start,graph,k):
    n=len(graph)
    v=[]
    d=[INF]*n  # 최단 거리
    heapq.heappush(v,[0,start]) # 시작 노드 큐에 삽입
    dict={}
    for i in range(1,len(graph)):
        dict.setdefault(i,[])
    while v:
        tmpv,tmpi=heapq.heappop(v)
        if d[tmpi]<tmpv:
            continue
        else:
            d[tmpi]=tmpv
        for i in range(n):  # 방문 노드를 거쳐 다른 노드로 가는 최단 거리 갱신
            next=d[tmpi]+graph[tmpi][i]
            if next<d[i]: # 시작점->방문노드 + 방문노드->다른노드 < 시작점->다른노드
                d[i]=next # 최단 거리 갱신
                dict[i].append(tmpi)
                heapq.heappush(v,[d[i],i])  # 인접노드 큐에 삽입
    return d[k]

def solution(n, s, a, b, fares):
    graph=[[INF for _ in range(n+1)] for _ in range(n+1)]
    for u,v,w in fares:
        graph[u][v]=w
        graph[v][u]=w
    cnt=INF
    for i in range(1,n+1):
        tmp=dijkstra(s, graph, i) + dijkstra(i, graph, a) + dijkstra(i, graph, b)
        if cnt>tmp:
            cnt=tmp
    return cnt

n=6
s=4
a=6
b=2
fares=[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n,s,a,b,fares))