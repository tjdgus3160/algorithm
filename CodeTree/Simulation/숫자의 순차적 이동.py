import sys
input=sys.stdin.readline

dx=[0,0,1,-1,1,1,-1,-1]
dy=[1,-1,0,0,-1,1,-1,1]

def find(num):
    x,y=loc[num]
    res=0
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            res=max(res,arr[ny][nx])
    return res

n,m=map(int,input().split())
arr=[]
loc={}
for y in range(n):
    tmp=[*map(int,input().split())]
    for x in range(n):
        loc[tmp[x]]=[x,y]
    arr.append(tmp)

for _ in range(m):
    for num in range(1,n*n+1):
        k=find(num)
        nx,ny=loc[num]
        kx,ky=loc[k]
        arr[ny][nx],arr[ky][kx]=arr[ky][kx],arr[ny][nx]
        loc[num],loc[k]=loc[k],loc[num]
for i in arr:
    print(*i)