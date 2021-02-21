# 13565번
from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(x,y):
    dq=deque([(x,y)])
    while dq:
        x,y=dq.pop()
        arr[y][x]=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and arr[ny][nx]=='0':
                if ny==m-1:
                    return True
                dq.append((nx,ny))
    return False

m,n=map(int,input().split())
arr=[]
for i in range(m):
    arr.append(list(input().rstrip('\n')))
for i in range(n):
    if arr[0][i]=='0' and dfs(i,0):
        print('YES')
        break
else:
    print('NO')