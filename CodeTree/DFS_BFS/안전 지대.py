from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y,k,visited):
    dq=deque([[x, y]])
    visited[y][x]=True
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and arr[ny][nx]>k and not visited[ny][nx]:
                visited[ny][nx]=True
                dq.append((nx,ny))

n,m=map(int,input().split())
arr=[]
k=0
for _ in range(n):
    tmp=[*map(int,input().split())]
    k=max(k,max(tmp))
    arr.append(tmp)
res=[]
for i in range(1,k+1):
    cnt=0
    visited=[[False]*m for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if arr[y][x]>i and not visited[y][x]:
                cnt+=1
                bfs(x,y,i,visited)
    res.append([i,cnt])
print(*sorted(res,key=lambda x:(-x[1],x[0]))[0])