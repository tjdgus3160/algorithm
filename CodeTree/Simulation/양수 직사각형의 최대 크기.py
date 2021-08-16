import sys
input=sys.stdin.readline

def func(sx,ex,sy,ey):
    global res
    for y in range(sy,ey+1):
        for x in range(sx,ex+1):
            if arr[y][x]<=0:
                return
    res=max(res,(ex-sx+1)*(ey-sy+1))

n,m=map(int,input().split())
arr=[[*map(int,input().split())]for _ in range(n)]
res=-1
for sy in range(n):
    for sx in range(m):
        for ey in range(sy,n):
            for ex in range(sx,m):
                func(sx,ex,sy,ey)
print(res)