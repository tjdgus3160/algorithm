from collections import deque
import sys
input=sys.stdin.readline

def find(x,y):
    cnt=0
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<9 and 0<=ny<9 and graph[ny][nx]==1:
            cnt+=1
    return cnt

def bfs(y,x):
    q=deque([(x,y)])
    while q:
        x,y=q.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<9 and 0<=ny<9 and graph[ny][nx]!=1 and res[ny][nx]=='_':
                res[ny][nx] = find(nx, ny)
                if res[ny][nx]==0:
                    q.append((nx, ny))
graph=[]
for i in range(9):
    graph.append([*map(int,input().split())])
r,c=map(int,input().split())

res=[['_']*9 for _ in range(9)]

# 방향 벡터(상하좌우4,대각선4)
dx=[0,1,0,-1,1,1,-1,-1]
dy=[1,0,-1,0,1,-1,-1,1]

if graph[r-1][c-1]==0:
    res[r - 1][c - 1]=find(c-1,r-1)
    if res[r-1][c-1]==0:
        bfs(r-1,c-1)
else:
    res[r-1][c-1]=-1

for i in res:
    print(*i)



