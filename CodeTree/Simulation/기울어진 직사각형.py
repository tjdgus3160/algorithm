import sys
input=sys.stdin.readline

def vaild(x,y):
    return 0<=x<n and 0<=y<n

dx=[1,-1,-1,1]
dy=[-1,-1,1,1]

def check(x,y,i,j):
    global res
    move=[i,j,i,j]
    k=0
    for d in range(4):
        for _ in range(move[d]):
            nx=x+dx[d]
            ny=y+dy[d]
            if not vaild(nx,ny):
                return
            k+=arr[ny][nx]
            x,y=nx,ny
    res=max(res,k)

n=int(input())
arr=[[*map(int,input().split())]for _ in range(n)]
res=0
for y in range(n):
    for x in range(n):
        for i in range(1,n): # 가로 이동 수
            for j in range(1,n): # 세로 이동 수
                check(x,y,i,j)
print(res)