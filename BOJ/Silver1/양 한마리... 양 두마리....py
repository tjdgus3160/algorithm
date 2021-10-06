# 14716번
from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    dq=deque([(x,y)])
    arr[x][y]='.'
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]=='#':
                arr[nx][ny]='.'
                dq.append((nx,ny))

for _ in range(int(input())):
    n,m=map(int,input().split())
    arr=[list(input().rstrip()) for _ in range(n)]
    res=0
    for x in range(n):
        for y in range(m):
            if arr[x][y]=='#':
                res+=1
                bfs(x,y)
    print(res)
