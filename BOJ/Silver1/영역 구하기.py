# 2583번
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x,y):
    c=0
    if 0 <= x < n and 0 <= y < m and arr[y][x]:
        arr[y][x]=0
        c+=1
        c+=dfs(x+1,y)
        c+=dfs(x-1,y)
        c+=dfs(x,y-1)
        c+=dfs(x,y+1)
    return c

m,n,k=map(int,input().split())
arr=[[1]*n for _ in range(m)]
for _ in range(k):
    sx,sy,ex,ey=map(int,input().split())
    for y in range(sy,ey):
        for x in range(sx,ex):
            arr[m-y-1][x]=0

res=[]
for y in range(m):
    for x in range(n):
        if arr[y][x]:
            res.append(dfs(x, y))
print(len(res))
print(*sorted(res))