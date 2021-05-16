# 6118번
from collections import deque,defaultdict
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
dist=defaultdict(list)
for _ in range(m):
    a,b=map(int,input().split())
    dist[a].append(b)
    dist[b].append(a)
visited=[False]*(n+1)
visited[1]=True
dq=deque([[1,0]])
cnt=1
while dq:
    if cnt==n:
        break
    k=len(dq)
    while k:
        v,t=dq.popleft()
        for i in dist[v]:
            if not visited[i]:
                dq.append([i,t+1])
                visited[i]=True
                cnt+=1
        k-=1
res=sorted(dq,key=lambda x:x[0])
print(res[0][0],res[0][1],len(res))
