# 1743번
from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    arr[y][x]=0
    res=1
    dq=deque([(x,y)])
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and arr[ny][nx]:
                arr[ny][nx]=0
                res+=1
                dq.append((nx,ny))
    return res

n,m,k=map(int,input().split())
arr=[[0]*m for _ in range(n)]
for _ in range(k):
    a,b=map(int,input().split())
    arr[a-1][b-1]=1
res=0
for y in range(n):
    for x in range(m):
        if arr[y][x]:
            res=max(res,bfs(x,y))
print(res)