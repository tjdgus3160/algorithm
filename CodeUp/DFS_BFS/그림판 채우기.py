from collections import deque
import sys
input=sys.stdin.readline

def bfs(x,y):
    q=deque([(x,y)])

    while q:
        x,y=q.popleft()
        graph[y][x]='*'
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<10 and 0<=ny<10 and graph[ny][nx]=='_':
                q.append((nx,ny))
                graph[ny][nx]='*'

graph=[]
for i in range(10):
    graph.append(list(input()[:-1]))
x,y=map(int,input().split())

# 방향 벡터
dx=[0,1,0,-1]
dy=[1,0,-1,0]

if graph[y][x]=='_':
    bfs(x,y)
for i in graph:
    print("".join(i))

