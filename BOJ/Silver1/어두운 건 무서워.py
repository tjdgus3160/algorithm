# 16507번
import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
arr=[[0]*(m+1)]
for x in range(n):
    arr.append([0,*map(int,input().split())])
    for y in range(m):
        arr[x+1][y+1]+=arr[x][y+1]+arr[x+1][y]-arr[x][y]
for _ in range(k):
    r1,c1,r2,c2=map(int,input().split())
    print((arr[r2][c2]-arr[r1-1][c2]-arr[r2][c1-1]+arr[r1-1][c1-1])//((r2-r1+1)*(c2-c1+1)))