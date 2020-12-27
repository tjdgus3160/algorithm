# 1260번
import sys
input=sys.stdin.readline

def bfs(v):
    q=[v]
    res=[]
    while q:
        node=q.pop(0)
        if node not in res:
            res.append(node)
            q+=graph[node]
    print(*res)

def dfs(v):
    visited.append(v)
    for i in graph[v]:
        if i not in visited:
            dfs(i)

n,m,v=map(int,input().split())
graph={}
for i in range(1,n+1):
    graph.setdefault(i,[])
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,n+1):
    graph[i].sort()
visited=[]
dfs(v)
print(*visited)
bfs(v)