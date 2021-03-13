# 2468번
from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y,k):
    dq=deque([(x,y)])
    visited[y][x]=True
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and arr[ny][nx] and not visited[ny][nx]:
                dq.append((nx,ny))
                visited[ny][nx]=True

n=int(input())
arr=[]
for _ in range(n):
    arr.append([*map(int,input().split())])
visited=[]
k=1
res=1
while True:
    for y in range(n):
        for x in range(n):
            if arr[y][x]<=k:
                arr[y][x]=0
    visited=[[False]*n for _ in range(n)]
    cnt=0
    for y in range(n):
        for x in range(n):
            if arr[y][x] and not visited[y][x]:
                bfs(x,y,k)
                cnt+=1
    if cnt==0:
        break
    k+=1
    res=max(res,cnt)
print(res)