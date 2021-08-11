from collections import deque
import sys
input=sys.stdin.readline

dx=[-2,-2,-1,-1,1,1,2,2]
dy=[-1,1,-2,2,-2,2,-1,1]

n=int(input())
sy,sx,ey,ex=map(lambda x:int(x)-1,input().split())
dq=deque([[sx,sy]])
visited=[[-1]*n for _ in range(n)]
visited[sy][sx]=0
while dq:
    x,y=dq.popleft()
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if visited[ny][nx]==-1 or visited[ny][nx]>visited[y][x]+1:
                visited[ny][nx]=visited[y][x]+1
                dq.append((nx,ny))
print(visited[ey][ex])