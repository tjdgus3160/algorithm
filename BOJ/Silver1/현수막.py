# 14716번
from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,1,-1,1,1,-1,-1]
dy=[1,-1,0,0,1,-1,-1,1]

def bfs(x,y):
    dq=deque([(x,y)])
    arr[x][y]=0
    while dq:
        x,y=dq.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]:
                arr[nx][ny]=0
                dq.append((nx,ny))

n,m=map(int,input().split())
arr=[[*map(int,input().split())] for _ in range(n)]

res=0
for x in range(n):
    for y in range(m):
        if arr[x][y]:
            res+=1
            bfs(x,y)
print(res)
