# 3184번
from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    global s,w
    sc,wc=0,0
    if arr[y][x]=='v':
        wc+=1
    else:
        sc+=1
    dq=deque([(x,y)])
    arr[y][x] = '#'
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<c and 0<=ny<r and arr[ny][nx] in '.vo':
                if arr[ny][nx]=='v':
                    wc+=1
                elif arr[ny][nx]=='o':
                    sc+=1
                arr[ny][nx] = '#'
                dq.append((nx,ny))
    if wc>=sc:
        w+=wc
    else:
        s+=sc

r,c=map(int,input().split())
arr=[]
for _ in range(r):
    arr.append(list(input().rstrip('\n')))

s,w=0,0
for y in range(r):
    for x in range(c):
        if arr[y][x] in 'vo':
            bfs(x,y)
print(s,w)