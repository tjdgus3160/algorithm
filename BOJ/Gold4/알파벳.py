# 1987번
import sys
input=sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,-1,0,1]

r,c=map(int,input().split())
arr=[input().rstrip() for _ in range(r)]
res=1
q=set([(0,0,arr[0][0])])
while q and res<26:
    x,y,k=q.pop()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<c and 0<=ny<r and arr[ny][nx] not in k:
            q.add((nx,ny,k+arr[ny][nx]))
            res=max(res,len(k)+1)
print(res)