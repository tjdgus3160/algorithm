# 2667번
from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(x,y):
    arr[y][x]=0
    dq=deque([(x,y)])
    res=1
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and arr[ny][nx]:
                arr[ny][nx]=0
                dq.append((nx,ny))
                res+=1
    return res

n=int(input())
arr=[]
for _ in range(n):
    arr.append([*map(int,list(input().rstrip('\n')))])
res=0
tmp=[]
for y in range(n):
    for x in range(n):
        if arr[y][x]:
            res+=1
            tmp.append(dfs(x,y))
print(res)
for i in sorted(tmp):
    print(i)