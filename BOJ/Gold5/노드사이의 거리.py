# 1240번
from collections import deque,defaultdict
import sys
input=sys.stdin.readline

def bfs(start,end):
    dq=deque([(start,0)])
    visted=[False]*(n+1)
    visted[start]=True
    while dq:
        node,dist=dq.popleft()
        if node==end:
            return dist
        for nxt,l in tree[node]:
            if not visted[nxt]:
                visted[nxt]=True
                dq.append((nxt,dist+l))

n,m=map(int,input().split())
tree=defaultdict(list)
for _ in range(n-1):
    u,v,w=map(int,input().split())
    tree[u].append((v,w))
    tree[v].append((u,w))
for _ in range(m):
    a,b=map(int,input().split())
    print(bfs(a,b))