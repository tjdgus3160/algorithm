n=int(input())
res=[[0]*n for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,-1,0,1]
d=0

k=n*n
y,x=n-1,n-1
while k:
    res[y][x]=k
    k-=1
    nx=x+dx[d]
    ny=y+dy[d]
    if not (0<=nx<n and 0<=ny<n and not res[ny][nx]):
        d=(d+1)%4
        nx = x + dx[d]
        ny = y + dy[d]
    x,y=nx,ny
for i in res:
    print(*i)