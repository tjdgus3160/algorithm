from collections import deque
import sys
input=sys.stdin.readline

def bfs(y,x):
    q=deque([(x,y)])

    while q:
        x,y=q.popleft()
        graph[y][x]='.'
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<w and 0<=ny<h and graph[ny][nx]=='L':
                q.append((nx,ny))
                graph[ny][nx]='.'

w,h=map(int,input().split())
graph=[]
for i in range(h):
    graph.append(list(input().split()))

# 방향 벡터
dx=[0,1,1,1,0,-1,-1,-1]
dy=[1,1,0,-1,-1,-1,0,1]
res=0
for i in range(h):
    for j in range(w):
        if graph[i][j]=='L':
            bfs(i,j)
            res+=1

print(res)
