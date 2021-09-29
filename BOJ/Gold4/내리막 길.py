# 1520번
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(x,y):
    if x==n-1 and y==m-1:
        return 1
    if dp[x][y]!=-1: # 이미 방문한 정점
        return dp[x][y]
    dp[x][y]=0 # 처음 방문
    for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if 0<=nx<n and 0<=ny<m and arr[x][y]>arr[nx][ny]:
            dp[x][y]+=dfs(nx,ny)
    return dp[x][y]

n,m=map(int,input().split())
arr=[[*map(int,input().split())]for _ in range(n)]
dp=[[-1]*m for _ in range(n)]
print(dfs(0,0))