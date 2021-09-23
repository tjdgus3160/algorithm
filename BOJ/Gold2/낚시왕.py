# 17143번
import sys
input=sys.stdin.readline

dx=[0,0,0,1,-1]
dy=[0,-1,1,0,0]

def changeD(d):
    if d==1: return 2
    if d==2: return 1
    if d==3: return 4
    if d==4: return 3

def move():
    tmp=[[[]for _ in range(m)] for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if arr[y][x]:
                k,d,_=arr[y][x]
                nx,ny=x,y
                while k:
                    if not (0<=nx+dx[d]<m and 0<=ny+dy[d]<n):
                        d=changeD(d)
                    nx+=dx[d]
                    ny+=dy[d]
                    k-=1
                arr[y][x][1]=d
                if tmp[ny][nx]:
                    if tmp[ny][nx][2]<arr[y][x][2]:
                        tmp[ny][nx] = arr[y][x]
                else:
                    tmp[ny][nx]=arr[y][x]
    return tmp

n,m,k=map(int,input().split())
arr=[[[]for _ in range(m)] for _ in range(n)]
for _ in range(k):
    y,x,dist,d,size=map(int,input().split())
    if d<=2:
        dist %= (n-1) * 2
    else:
        dist %= (m-1) * 2
    arr[y-1][x-1]=[dist,d,size]
res=0
for i in range(m):
    for j in range(n):
        if arr[j][i]:
            res+=arr[j][i][2]
            arr[j][i]=[]
            break
    arr=move()
print(res)