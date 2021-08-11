from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    k=arr[y][x]
    dq=deque([[x, y]])
    arr[y][x]=0
    cnt=1
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and arr[ny][nx]==k:
                cnt+=1
                arr[ny][nx]=0
                dq.append((nx,ny))
    return cnt

n=int(input())
arr=[[*map(int,input().split())] for _ in range(n)]
res=[0,0]

for y in range(n):
    for x in range(n):
        if arr[y][x]:
            cnt=bfs(x,y)
            res[1] = max(res[1], cnt)
            if cnt>3:
                res[0]+=1
print(*res)