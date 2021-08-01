# 10026번
from collections import deque
import sys
input=sys.stdin.readline

def bfs(x,y,c):
    dq=deque([[x,y]])
    tmp[y][x]=c
    while dq:
        x,y=dq.popleft()
        for nx,ny in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
            if 0<=nx<n and 0<=ny<n and arr[ny][nx]==c and not tmp[ny][nx]:
                tmp[ny][nx]=c
                dq.append([nx,ny])

def bfs2(x,y,c):
    dq=deque([[x,y]])
    tmp[y][x]=c
    while dq:
        x,y=dq.popleft()
        for nx,ny in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
            if 0<=nx<n and 0<=ny<n and arr[ny][nx] in 'RG' and not tmp[ny][nx]:
                tmp[ny][nx]=c
                dq.append([nx,ny])

n=int(input())
arr=[input().rstrip() for _ in range(n)]

res=[0,0]

tmp=[[0]*n for _ in range(n)]
for y in range(n):
    for x in range(n):
        if not tmp[y][x]:
            res[0]+=1
            bfs(x,y,arr[y][x])
tmp=[[0]*n for _ in range(n)]
for y in range(n):
    for x in range(n):
        if not tmp[y][x]:
            res[1]+=1
            if arr[y][x]=='B':
                bfs(x, y, arr[y][x])
            else:
                bfs2(x,y,arr[y][x])

print(*res)