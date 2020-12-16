# 1926번
from _collections import deque
import sys
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def dfs(y,x):
    q=deque([(x,y)])
    arr[y][x]=0
    res=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and arr[ny][nx]:
                q.append((nx,ny))
                arr[ny][nx]=0
                res+=1
    return res

n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append([*map(int,input().split())])
cnt=0
size=0
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            t=dfs(i,j)
            size=max(size,t)
            cnt+=1
print(cnt)
print(size)