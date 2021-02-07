# 4963번
from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,1,-1,1,1,-1,-1]
dy=[1,-1,0,0,-1,1,-1,1]

def bfs(x,y):
    dq=deque([(x,y)])
    arr[y][x]=0
    while dq:
        x,y=dq.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<w and 0<=ny<h and arr[ny][nx]:
                arr[ny][nx]=0
                dq.append((nx,ny))
while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    arr=[]
    res=0
    for _ in range(h):
        arr.append([*map(int,input().split())])
    for y in range(h):
        for x in range(w):
            if arr[y][x]:
                bfs(x,y)
                res+=1
    print(res)