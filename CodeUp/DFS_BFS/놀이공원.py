from collections import deque
import sys
input=sys.stdin.readline

def bfs(y,x):
    global n,m
    q=deque([(x,y)])
    graph[y][x]*=-1
    res=0
    while q:
        cnt=len(q)
        res+=1
        while cnt>0:
            cnt-=1
            x,y=q.popleft()
            if x==m-1 and y==n-1:
                return res
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<m and 0<=ny<n and abs(graph[y][x]+graph[ny][nx])<2 and graph[ny][nx]>0:
                    graph[ny][nx]=-graph[ny][nx]
                    q+=[(nx,ny)]
    return res if graph[n-1][m-1]<0 else 0

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph+=[[*map(int,input().split())]]


# 방향 벡터(상하좌우4,대각선4)
dx=[0,1,0,-1]
dy=[1,0,-1,0]

print(bfs(0,0))
