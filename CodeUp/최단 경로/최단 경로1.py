import heapq
import sys
input=sys.stdin.readline
INF=sys.maxsize

def find(start,end):
    v=[]
    heapq.heappush(v,[0,start])
    d[start]=0
    while v:
        tmpv,tmpi=heapq.heappop(v)
        if d[tmpi]<tmpv:
            continue
        else:
            d[tmpi]=tmpv
        for i in graph:
            if i in graph[tmpi]:
                next=d[tmpi]+graph[tmpi][i]
                if next<d[i]:
                    d[i]=next
                    heapq.heappush(v,[d[i],i])
    if d[end]!=INF:
        print(d[end])
    else:
        print(-1)

n,m=map(int,input().split())
graph = {}
trace = {}
d = {}
for i in range(n):
    graph.setdefault(chr(65+i),{})
    d.setdefault(chr(65+i),INF)

for _ in range(m):
    a,b,c=input().split()
    graph[a][b]=int(c)
    graph[b][a]=int(c)

start,end=input().split()
find(start,end)
