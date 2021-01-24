# 2606번
from collections import deque
import sys
input=sys.stdin.readline

def bfs(start):
    dq=deque([start])
    visited[start]=True
    res=0
    while dq:
        t=dq.popleft()
        for i in dic[t]:
            if not visited[i]:
                dq.append(i)
                visited[i]=True
                res+=1
    return res

n=int(input())
visited=[False]*(n+1)
dic={}
for i in range(1,n+1):
    dic.setdefault(i,[])
for _ in range(int(input())):
    a,b=map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)

print(bfs(1))