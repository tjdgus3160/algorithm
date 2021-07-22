# 1967번
from collections import defaultdict,deque
import sys
input=sys.stdin.readline

def dfs(start):
    global res
    farthest_node=start
    visited=[False]*(n+1)
    dq=deque([[start,0]])
    visited[start]=True
    while dq:
        node,k=dq.popleft()
        if k>res:
            res=k
            farthest_node=node
        for i in tree[node]:
            if not visited[i]:
                dq.append([i,k+tree[node][i]])
                visited[i]=True
    return farthest_node

res=0
tree=defaultdict(dict)
n=int(input())
for _ in range(n-1):
    a,b,w=map(int,input().split())
    tree[a][b]=w
    tree[b][a]=w

farthest_node=dfs(1)
dfs(farthest_node)
print(res)