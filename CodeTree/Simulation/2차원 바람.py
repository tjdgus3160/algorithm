import sys
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def avg(x,y):
    k=[arr[y][x]]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n:
            k.append(arr[ny][nx])
    return sum(k)//len(k)

n,m,q=map(int,input().split())
arr=[[*map(int,input().split())] for _ in range(n)]
for _ in range(q):
    sy,sx,ey,ex=map(lambda x:(int(x)-1),input().split())
    tmp=[arr[y][sx:ex+1] for y in range(sy,ey+1)]
    tmp[0]=[arr[sy+1][sx]]+arr[sy][sx:ex]
    for y in range(sy+1,ey):
        tmp[y-sy][0]=arr[y+1][sx]
        tmp[y-sy][-1]=arr[y-1][ex]
    tmp[-1]=arr[ey][sx+1:ex+1]+[arr[ey-1][ex]]
    for y in range(ey-sy+1):
        for x in range(ex-sx+1):
            arr[y+sy][x+sx]=tmp[y][x]

    for y in range(ey-sy+1):
        for x in range(ex-sx+1):
            tmp[y][x]=avg(x+sx,y+sy)

    for y in range(ey-sy+1):
        for x in range(ex-sx+1):
            arr[y+sy][x+sx]=tmp[y][x]
for i in arr:
    print(*i)