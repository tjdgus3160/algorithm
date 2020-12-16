# 7576번
from _collections import deque
import sys
input=sys.stdin.readline

m,n=map(int,input().split())
arr=[]
total=0
cnt=0
q=deque()
for i in range(n):
    l=[*map(int,input().split())]
    arr.append(l)
    for j in range(m):
        if l[j]==1:
            q.append((j,i))
            cnt+=1
        if l[j]!=-1:
            total+=1

dx=[-1,1,0,0]
dy=[0,0,1,-1]
day=-1
while q:
    k=len(q)
    while k>0:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and arr[ny][nx]==0:
                q.append((nx,ny))
                arr[ny][nx]=1
                cnt+=1
        k-=1
    day+=1
print(day if total==cnt else -1)