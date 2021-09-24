# 1913번
import sys
input=sys.stdin.readline

dx=[1,0,-1,0]
dy=[0,1,0,-1]
d=0

n=int(input())
k=int(input())
arr=[[0]*n for _ in range(n)]
cur=n*n
x,y=0,0
res=[]
while cur:
    arr[x][y]=cur
    if cur==k:
        res=[x+1,y+1]
    cur-=1
    nx,ny=x+dx[d],y+dy[d]
    if not(0<=nx<n and 0<=ny<n) or arr[nx][ny]:
        d=(d+1)%4
        nx,ny=x+dx[d],y+dy[d]
    x,y=nx,ny
for i in arr:
    print(*i)
print(*res)