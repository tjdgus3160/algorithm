# 7569번
from collections import deque
import sys
input=sys.stdin.readline

m,n,h=map(int,input().split())
tomato=deque()
cnt=0
arr=[]
for i in range(h):
    tmp=[]
    for y in range(n):
        s=[*map(int,input().split())]
        for x in range(m):
            if s[x]==1:
                tomato.append([i,x,y])
            if not s[x]:
                cnt+=1
        tmp.append(s)
    arr.append(tmp)
if not cnt:
    print(0)
    exit()

res=0
while tomato:
    res+=1
    for _ in range(len(tomato)):
        z,x,y=tomato.popleft()
        for nz,nx,ny in [[z+1,x,y],[z-1,x,y],[z,x+1,y],[z,x-1,y],[z,x,y+1],[z,x,y-1]]:
            if 0<=nz<h and 0<=nx<m and 0<=ny<n and not arr[nz][ny][nx]:
                cnt-=1
                arr[nz][ny][nx]=1
                tomato.append([nz,nx,ny])
if cnt:
    print(-1)
else:
    print(res-1)