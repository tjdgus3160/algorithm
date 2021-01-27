# 13901번
from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,0,-1,1]
dy=[0,-1,1,0,0]
r,c=map(int,input().split())
arr=[]
for _ in range(r):
    arr.append(['*']*c)
for _ in range(int(input())):
    y,x=map(int,input().split())
    arr[y][x]='x'
sy,sx=map(int,input().split())
arr[sy][sx]=1
dq=deque([*map(int,input().split())])
while True:
    flag=True
    for _ in range(4):
        direct=dq.popleft()
        dq.append(direct)
        nx=sx+dx[direct]
        ny=sy+dy[direct]
        while 0<=nx<c and 0<=ny<r and arr[ny][nx]=='*':
            arr[ny][nx] = 1
            sx,sy=nx,ny
            flag=False
            nx+=dx[direct]
            ny+=dy[direct]
    if flag:
        print(sy,sx)
        break
