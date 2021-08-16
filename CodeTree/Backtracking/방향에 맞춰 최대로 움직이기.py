import sys
input=sys.stdin.readline

dx=[0,0,1,1,1,0,-1,-1,-1]
dy=[0,-1,-1,0,1,1,1,0,-1]

def vaild(x,y):
    return 0<=x<n and 0<=y<n

def func(x,y,cnt):
    global res
    k=d[y][x]
    cur=arr[y][x]
    while True:
        nx=x+dx[k]
        ny=y+dy[k]
        if not vaild(nx,ny):
            break
        if arr[ny][nx]>cur:
            func(nx,ny,cnt+1)
        x,y=nx,ny
    res=max(res,cnt)

n=int(input())
arr=[[*map(int,input().split())]for _ in range(n)]
d=[[*map(int,input().split())]for _ in range(n)]
y,x=map(lambda x:int(x)-1,input().split())
res=0
func(x,y,0)
print(res)