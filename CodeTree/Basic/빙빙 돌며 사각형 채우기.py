import string

n,m=map(int,input().split())
res=[[0]*m for _ in range(n)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]
d=0

k=0
y,x=0,0
alp=string.ascii_uppercase
while k<n*m:
    res[y][x]=alp[k%26]
    k+=1
    nx=x+dx[d]
    ny=y+dy[d]
    if not (0<=nx<m and 0<=ny<n and not res[ny][nx]):
        d=(d+1)%4
        nx = x + dx[d]
        ny = y + dy[d]
    x,y=nx,ny
for i in res:
    print(*i)