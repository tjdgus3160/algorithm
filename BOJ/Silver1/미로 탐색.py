# 2178번
from collections import deque
import sys
input=sys.stdin.readline

def bfs(y,x):
    q=deque()
    q.append((x,y))

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and arr[ny][nx]==1:
                q.append((nx,ny))
                arr[ny][nx]=arr[y][x]+1
    return arr[n-1][m-1]

n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append([*map(int,list(input()[:-1]))])

dx=[0,0,1,-1]
dy=[1,-1,0,0]
print(bfs(0,0))
