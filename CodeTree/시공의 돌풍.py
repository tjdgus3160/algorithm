import sys
input=sys.stdin.readline

def diffuse(x,y,tmp):
    k=arr[y][x]//5
    loc=[[nx,ny] for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] if 0<=nx<m and 0<=ny<n and arr[ny][nx]!=-1]
    tmp[y][x]+=arr[y][x]-(k*len(loc))
    for nx,ny in loc:
        tmp[ny][nx]+=k

def rotate(wind,tmp):
    for y in range(wind[0][1]-1,0,-1):
        tmp[y][0]=tmp[y-1][0]
    tmp[0][:m-1]=tmp[0][1:]
    for y in range(wind[0][1]):
        tmp[y][-1]=tmp[y+1][-1]
    tmp[wind[0][1]][1:]=[0]+tmp[wind[0][1]][1:-1]
    for y in range(wind[1][1]+1,n-1):
        tmp[y][0]=tmp[y+1][0]
    tmp[-1][:-1]=tmp[-1][1:]
    for y in range(n-1,wind[1][1],-1):
        tmp[y][-1]=tmp[y-1][-1]
    tmp[wind[1][1]][1:]=[0]+tmp[wind[1][1]][1:-1]

n,m,t=map(int,input().split())
arr=[]
wind=[]
for y in range(n):
    tmp=[*map(int,input().split())]
    arr.append(tmp)
    if len(wind)==2:
        continue
    for x in range(m):
        if tmp[x]==-1:
            wind.append([x,y])
            break

for _ in range(t):
    tmp=[[0]*m for _ in range(n)]
    tmp[wind[0][1]][wind[0][0]]=-1
    tmp[wind[1][1]][wind[1][0]]=-1
    for y in range(n):
        for x in range(m):
            if arr[y][x]!=-1:
                diffuse(x,y,tmp)
    rotate(wind,tmp)
    arr=tmp
print(sum([sum(i) for i in arr])+2)