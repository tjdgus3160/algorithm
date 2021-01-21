# 11725번
from collections import deque
import sys
input=sys.stdin.readline

tree={}

n=int(input())
res=[0]*(n+1)
visited=[False]*(n+1)
for _ in range(n-1):
    a,b=map(int,input().split())
    tree.setdefault(a,[])
    tree.setdefault(b,[])
    tree[a].append(b)
    tree[b].append(a)

dq=deque()
visited[1]=True
for i in tree[1]:
    if not visited[i]:
        dq.append(i)
        res[i]=1
        visited[i]=True
while dq:
    k=dq.popleft()
    for i in tree[k]:
        if not visited[i]:
            dq.append(i)
            res[i]=k
            visited[i] = True
for i in res[2:]:
    print(i)