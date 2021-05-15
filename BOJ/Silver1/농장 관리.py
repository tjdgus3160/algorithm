# 1245번
from collections import deque
import sys
input=sys.stdin.readline

dx=[0,1,1,1,0,-1,-1,-1]
dy=[-1,-1,0,1,1,1,0,-1]

tmp=[]

def check(x,y,k):
    dq=deque([[x,y]])
    s=deque([[x,y]])
    while dq:
        x,y=dq.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and [nx,ny] not in s:
                if arr[ny][nx]==k:
                    dq.append([nx,ny])
                    s.append([nx,ny])
                elif arr[ny][nx]>k:
                    return False
    tmp.extend(s)
    return True

n,m=map(int,input().split())
arr=[[*map(int,input().split())] for _ in range(n)]

res=0
for y in range(n):
    for x in range(m):
        if arr[y][x] and [x,y] not in tmp and check(x,y,arr[y][x]):
            res+=1
print(res)