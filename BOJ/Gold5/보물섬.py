# 2589번
from collections import deque
import sys
input=sys.stdin.readline

def bfs(x,y):
    dq=deque([(x,y,0)])
    visited=[[False]*m for _ in range(n)]
    visited[x][y]=True
    res=0
    while dq:
        x,y,k=dq.popleft()
        for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if 0<=nx<n and 0<=ny<m and board[nx][ny]=='L' and not visited[nx][ny]:
                visited[nx][ny]=True
                dq.append((nx,ny,k+1))
                res=max(res,k+1)
    return res

n,m=map(int,input().split())
board=[input().rstrip() for _ in range(n)]

res=0
for x in range(n):
    for y in range(m):
        if board[x][y]=='L':
            res=max(res,bfs(x,y))
print(res)
