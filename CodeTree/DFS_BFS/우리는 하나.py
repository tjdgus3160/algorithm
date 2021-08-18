from collections import deque
from itertools import combinations
import sys
input=sys.stdin.readline

def bfs(start):
    dq=deque(start)
    tmp=[[False]*n for _ in range(n)]
    for x,y in start:
        tmp[y][x]=True
    cnt=len(start)
    while dq:
        x,y=dq.popleft()
        for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if 0<=nx<n and 0<=ny<n and u<=abs(arr[y][x]-arr[ny][nx])<=d and not tmp[ny][nx]:
                tmp[ny][nx]=True
                cnt+=1
                dq.append((nx,ny))
    return cnt

n,k,u,d=map(int,input().split())
city=[(x,y) for x in range(n) for y in range(n)]
arr=[[*map(int,input().split())]for _ in range(n)]
res=0
for sub in combinations(city,k):
    res=max(res,bfs(sub))
print(res)