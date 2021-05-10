# 21736번
from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

n,m=map(int,input().split())
arr=[]
x,y=0,0
for i in range(n):
    line=input().rstrip()
    if 'I' in line:
        x,y=line.index('I'),i
    arr.append(line)
res=0
dq=deque([[x,y]])
visited=[[False]*m for _ in range(n)]
visited[y][x]=True
while dq:
    x,y=dq.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n and not visited[ny][nx] and arr[ny][nx]!='X':
            dq.append([nx,ny])
            visited[ny][nx]=True
            if arr[ny][nx]=='P':
                res+=1
print(res if res else 'TT')
