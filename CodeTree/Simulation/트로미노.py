import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[[*map(int,input().split())] for _ in range(n)]
res=0
for y in range(n):
    for x in range(m-2):
        res=max(res,arr[y][x]+arr[y][x+1]+arr[y][x+2])
for y in range(n-2):
    for x in range(m):
        res=max(res,arr[y][x]+arr[y+1][x]+arr[y+2][x])
for y in range(n-1):
    for x in range(m-1):
        res=max(res,arr[y][x]+arr[y+1][x]+arr[y+1][x+1])
for y in range(n-1):
    for x in range(m-1):
        res=max(res,arr[y][x]+arr[y+1][x]+arr[y][x+1])
for y in range(n-1):
    for x in range(m-1):
        res=max(res,arr[y][x]+arr[y][x+1]+arr[y+1][x+1])
for y in range(n-1):
    for x in range(1,m):
        res=max(res,arr[y][x]+arr[y+1][x]+arr[y+1][x-1])
print(res)