# 14502번
from itertools import combinations
from copy import deepcopy
from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs():
    global res
    dq=deque(virus)
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and not tmp[ny][nx]:
                tmp[ny][nx]=2
                dq.append([nx,ny])
    res=max(res,sum([i.count(0) for i in tmp]))

n,m=map(int,input().split())
arr=[]
safe=[]
virus=[]
res=0
for y in range(n):
    tmp=[*map(int,input().split())]
    arr.append(tmp)
    for x in range(len(tmp)):
        if not tmp[x]:
            safe.append([x,y])
        elif tmp[x]==2:
            virus.append([x,y])

for sub in combinations(safe,3):
    tmp=deepcopy(arr)
    for x,y in sub:
        tmp[y][x]=1
    bfs()
print(res)