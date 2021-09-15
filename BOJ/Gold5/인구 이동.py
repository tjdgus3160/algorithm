# 16234번
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(x,y):
    for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if 0<=nx<n and 0<=ny<n and l<=abs(arr[nx][ny]-arr[x][y])<=r and not visited[nx][ny]:
            visited[nx][ny]=True
            union.append((nx,ny))
            dfs(nx,ny)

n,l,r=map(int,input().split())
arr=[[*map(int,input().split())]for _ in range(n)]
res=0
while True:
    visited=[[False]*n for _ in range(n)]
    flag=False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union=[(i,j)]
                visited[i][j]=True
                dfs(i,j)
                if len(union)>1:
                    flag=True
                    k=sum([arr[x][y] for x,y in union])//len(union)
                    for x,y in union:
                        arr[x][y]=k
    if not flag:
        break
    res+=1
print(res)