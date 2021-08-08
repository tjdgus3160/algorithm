import sys
input=sys.stdin.readline

dx=[0,0,1,-1,1,1,-1,-1]
dy=[1,-1,0,0,1,-1,-1,1]

def find(x,y):
    mx,my=None,None
    k=0
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if not (0<=nx<n and 0<=ny<n):
            continue
        for v in arr[ny][nx]:
            if v>k:
                k=v
                mx,my=nx,ny
    return mx,my

def simulation(i):
    x,y=dic[i]
    nx,ny=find(x,y)
    if nx==None:
        return
    idx=arr[y][x].index(i)
    tmp=arr[y][x][:idx+1]
    for i in tmp:
        if i in dic:
            dic[i]=[nx,ny]
    arr[ny][nx]=tmp+arr[ny][nx]
    arr[y][x]=arr[y][x][idx+1:]

n,m=map(int,input().split())
arr=[]
for _ in range(n):
    t=[[i] for i in [*map(int,input().split())]]
    arr.append(t)
move=[*map(int,input().split())]

dic={}
for y in range(n):
    for x in range(n):
        if arr[y][x][0] in move:
            dic[arr[y][x][0]]=[x,y]

for i in move:
    simulation(i)

for y in range(n):
    for x in range(n):
        if not arr[y][x]:
            print(None)
        else:
            print(*arr[y][x])