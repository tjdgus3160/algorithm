# 1913번
import sys
input=sys.stdin.readline

n=int(input())
k=int(input())
arr=[[0 for _ in range(n)] for _ in range(n)]


x,y=n//2,n//2
d=0 # 상0 우1 하2 좌3
dx=[0,1,0,-1]
dy=[-1,0,1,0]
arr[y][x]=1
y-=1
cnt=2
while cnt<=n**2:
    arr[y][x]=cnt
    if cnt==k:
        res=[y+1,x+1]
    if d==0 and 0<=y+1<n and 0<=x+1<n and arr[y+1][x]>0 and arr[y][x+1]==0:
        d=1
    elif d==1 and 0<=y+1<n and 0<=x-1<n and arr[y][x-1]>0 and arr[y+1][x]==0:
        d=2
    elif d==2 and 0<=y-1<n and 0<=x-1<n and arr[y-1][x]>0 and arr[y][x-1]==0:
        d=3
    elif d==3 and 0<=y-1<n and 0<=x+1<n and arr[y][x+1]>0 and arr[y-1][x]==0:
        d=0
    cnt+=1
    y,x=y+dy[d],x+dx[d]
for a in arr:
    print(*a)
print(*res)
