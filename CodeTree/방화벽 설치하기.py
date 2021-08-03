from itertools import combinations
from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(fire):
    cnt=len(fire)
    visited=[[False]*m for _ in range(n)]
    dq=deque(fire)
    for x,y in fire:
        visited[y][x]=True
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and not arr[ny][nx] and not visited[ny][nx]:
                visited[ny][nx]=True
                dq.append([nx,ny])
                cnt+=1
    return cnt

n,m=map(int,input().split())
arr=[]
fire=[]
empty=[]
wall=0
for y in range(n):
    tmp=[*map(int,input().split())]
    for x in range(m):
        if not tmp[x]:
            empty.append((x,y))
        if tmp[x]==1:
            wall+=1
        elif tmp[x]==2:
            fire.append([x,y])
    arr.append(tmp)
res=0
for sub in combinations(empty,3):
    for x,y in sub:
        arr[y][x]=1
    k=bfs(fire)
    res=max(res,n*m-k-wall-3)
    for x,y in sub:
        arr[y][x]=0
print(res)