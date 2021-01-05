# 10157번
import sys
input=sys.stdin.readline

def func(k,total):
    x,y=0,r-1
    n=1
    d=0 # 0상 1하 2좌 3우
    while n<=total:
        arr[y][x]=n
        if n==k:
            print(x+1,r-y)
            return
        if d==0 and (y-1<0 or arr[y-1][x]):
            d=3
        elif d==1 and (y+1>=r or arr[y+1][x]):
            d=2
        elif d==2 and (x-1<0 or arr[y][x-1]):
            d=0
        elif d==3 and (x+1>=c or arr[y][x+1]):
            d=1
        x,y=x+dx[d],y+dy[d]
        n+=1
    print(0)
    return

dx=[0,0,-1,1]
dy=[-1,1,0,0]
c,r=map(int,input().split())
arr=[[0]*c for _ in range(r)]

func(int(input()),c*r)