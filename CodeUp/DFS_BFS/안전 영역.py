from collections import deque
import copy
import sys
input=sys.stdin.readline

def bfs(y,x,k):
    q=deque([(x,y)])
    v=[(x,y)]
    while q:
        x,y=q.popleft()
        tmp[y][x]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and tmp[ny][nx]>=k:
                q.append((nx,ny))
                v.append((nx,ny))
                tmp[ny][nx]=0

n=int(input())
graph=[]
ks=[]
for i in range(n):
    t=[*map(int,input().split())]
    graph.append(t)
    for j in t:
        if j not in ks:
            ks.append(j)

# 방향 벡터
dx=[0,1,0,-1]
dy=[1,0,-1,0]

res=0
for k in ks:
    tmp = copy.deepcopy(graph)
    cnt=0
    for i in range(n):
        for j in range(n):
            if tmp[i][j]>=k:
                bfs(i,j,k)
                cnt+=1
    res=max(res,cnt)
print(res)


