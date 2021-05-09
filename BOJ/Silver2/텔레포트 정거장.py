# 18232번
from collections import deque,defaultdict
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
s,e=map(int,input().split())
dic=defaultdict(list)
visited=[False]*300001
visited[e]=True
for _ in range(m):
    x,y=map(int,input().split())
    dic[x].append(y)
    dic[y].append(x)
dq=deque([[e,0]])
while dq:
    loc,time=dq.popleft()
    if loc==s:
        print(time)
        break
    if 1<=loc-1<=n and not visited[loc-1]:
        dq.append([loc-1,time+1])
        visited[loc-1]=True
    if 1 <= loc + 1 <= n and not visited[loc+1]:
        dq.append([loc + 1, time + 1])
        visited[loc+1]=True
    if loc in dic:
        for i in dic[loc]:
            if not visited[i]:
                dq.append([i,time+1])
                visited[i]=True