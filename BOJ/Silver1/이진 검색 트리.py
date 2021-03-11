# 5639번
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(start,k):
    global res
    if start!=1 and len(graph[start])==1:
        res+=k
        return
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i, k+1)

n=int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
res=0

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1]=True
dfs(1,0)
print('Yes' if res%2==1 else 'No')