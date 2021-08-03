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
                k,d,_=arr[y][x][0]
                nx,ny=x,y
                while k:
                    if not (0<=nx+dx[d]<m and 0<=ny+dy[d]<n):
                        d=changeD(d)
                    nx+=dx[d]
                    ny+=dy[d]
                    k-=1
                arr[y][x][0][1]=d
                tmp[ny][nx].append(arr[y][x][0])
    return tmp

def check():
    for y in range(n):
        for x in range(m):
            if len(arr[y][x])>1:
                tmp=arr[y][x][0]
                k=arr[y][x][0][2]
                for i in arr[y][x][1:]:
                    if i[2]>k:
                        tmp=i
                        k=i[2]
                arr[y][x]=[tmp]

n,m,k=map(int,input().split())
arr=[[[]for _ in range(m)] for _ in range(n)]
for _ in range(k):
    y,x,dist,d,size=map(int,input().split())
    arr[y-1][x-1].append([dist,d,size])
res=0
for i in range(m):
    for j in range(n):
        if arr[j][i]:
            res+=arr[j][i][0][2]
            arr[j][i]=[]
            break
    arr=move()
    check()
print(res)