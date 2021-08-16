import sys
input=sys.stdin.readline

def func(sx,ex,sy,ey):
    k=0
    for y in range(sy,ey+1):
        for x in range(sx,ex+1):
            k+=arr[y][x]
    return k

def vaild(sx1,ex1,sy1,ey1,sx2,ex2,sy2,ey2):
    tmp=[[False]*m for _ in range(n)]
    for y in range(sy1,ey1+1):
        for x in range(sx1,ex1+1):
            tmp[y][x]=True
    for y in range(sy2,ey2+1):
        for x in range(sx2,ex2+1):
            if tmp[y][x]:
                return False
    return True

def cal(sx1,sy1,ex1,ey1):
    global res
    first=func(sx1,ex1,sy1,ey1)
    second=-1*float('inf')
    for sy in range(n):
        for sx in range(m):
            for ey in range(sy,n):
                for ex in range(sx,m):
                    if vaild(sx1,ex1,sy1,ey1,sx,ex,sy,ey):
                        second=max(second,func(sx,ex,sy,ey))
    res=max(res,first+second)

n,m=map(int,input().split())
arr=[[*map(int,input().split())]for _ in range(n)]
res=-1*float('inf')
for sy in range(n):
    for sx in range(m):
        for ey in range(sy,n):
            for ex in range(sx,m):
                cal(sx,sy,ex,ey)
print(res)