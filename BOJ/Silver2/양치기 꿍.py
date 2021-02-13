# 3187번
from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y,v,k):
    dq=deque([[x,y]])
    arr[y][x]='#'
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<c and 0<=ny<r and arr[ny][nx] !='#':
                if arr[ny][nx]=='v':
                    v+=1
                elif arr[ny][nx]=='k':
                    k+=1
                arr[ny][nx]='#'
                dq.append([nx,ny])
    if v>=k:
        return v,0
    else:
        return 0,k

r,c=map(int,input().split())
arr=[]
for _ in range(r):
    arr.append(list(input().rstrip('\n')))
s,w=0,0
for y in range(r):
    for x in range(c):
        a,b=0,0
        if arr[y][x] == 'v':
            a,b=bfs(x,y,1,0)
        elif arr[y][x] == 'k':
            a,b=bfs(x,y,0,1)
        w+=a
        s+=b
print(s,w)