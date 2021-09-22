# 2636번
from collections import deque
import sys
input=sys.stdin.readline

def bfs(x,y,k):
    dq=deque([(x,y)])
    visited[x][y]=True
    while dq:
        x,y=dq.popleft()
        for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]==k and not visited[nx][ny]:
                visited[nx][ny]=True
                dq.append((nx,ny))



n,m=map(int,input().split())
arr=[[*map(int,input().split())]for _ in range(n)]

time=0
res=0
while True:
    visited = [[False] * m for _ in range(n)]
    bfs(0, 0, 0)
    cnt=0
    for x in range(n):
        for y in range(m):
            if arr[x][y]==1:
                cnt+=1
                for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
                        arr[x][y]=0
                        break
    if not cnt:
        break
    time+=1
    res=cnt
print(time)
print(res)