# 17086번
from collections import deque
import sys
input=sys.stdin.readline

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

def bfs(x,y):
    dq=deque([[x,y]])
    while dq:
        x,y=dq.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and arr[ny][nx]!=1:
                if arr[y][x]==1:
                    arr[ny][nx]=-1
                    dq.append([nx,ny])
                elif arr[ny][nx]==0 or  arr[ny][nx]<arr[y][x]-1:
                    arr[ny][nx]=arr[y][x]-1
                    dq.append([nx,ny])

n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append([*map(int,input().split())])
res=0
for y in range(n):
    for x in range(m):
        if arr[y][x]==1:
            bfs(x,y)
print(-1*min([min(i) for i in arr]))
