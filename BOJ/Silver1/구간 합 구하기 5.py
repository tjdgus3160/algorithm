# 11660번
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[[0]*(n+1)]
for x in range(n):
    arr.append([0,*map(int,input().split())])
    for y in range(n):
        arr[x+1][y+1]+=arr[x][y+1]+arr[x+1][y]-arr[x][y]
for _ in range(m):
    i,j,x,y=map(int,input().split())
    print(arr[x][y]-arr[i-1][y]-arr[x][j-1]+arr[i-1][j-1])