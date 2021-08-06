import sys
input=sys.stdin.readline

dx=[1,0,-1,0]
dy=[0,1,0,-1]
d=0

def check(x,y,d):
    return arr[y+dy[(d+1)%4]][x+dx[(d+1)%4]]=='#'

n=int(input())
sy,sx=map(int,input().split())
x,y=sx-1,sy-1
arr=[list(input().rstrip()) for _ in range(n)]
visited=[[[False]*4 for _ in range(n)] for _ in range(n)]
res=0
while 0<=x<n and 0<=y<n:
    if visited[y][x][d]:
        print(-1)
        exit()

    visited[y][x][d]=True

    nx,ny=x+dx[d],y+dy[d]
    if not (0<=nx<n and 0<=ny<n):
        res+=1
        break
    if arr[ny][nx]=='#':
        d=(d+3)%4
    elif check(nx,ny,d):
        x,y=nx,ny
        res += 1
    else:
        x,y=nx+dx[(d+1)%4],ny+dy[(d+1)%4]
        d=(d+1)%4
        res+=2
print(res)