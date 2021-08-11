from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    dq=deque([[x, y]])
    cnt=1
    arr[y][x]=0
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and arr[ny][nx]:
                dq.append((nx,ny))
                arr[ny][nx]=0
                cnt+=1
    return cnt

n=int(input())
arr=[[*map(int,input().split())] for _ in range(n)]
res=[]
for y in range(n):
    for x in range(n):
        if arr[y][x]:
            res.append(bfs(x,y))
print(len(res))
for i in sorted(res):
    print(i)