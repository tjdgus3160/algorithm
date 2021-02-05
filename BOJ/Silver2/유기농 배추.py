# 1012번
from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    dq=deque([(x,y)])
    arr[y][x]=0
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and arr[ny][nx]:
                arr[ny][nx]=0
                dq.append([nx,ny])

for _ in range(int(input())):
    m,n,k=map(int,input().split())
    arr=[[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x,y=map(int,input().split())
        arr[y][x]=1
    res=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                bfs(j,i)
                res+=1
    print(res)