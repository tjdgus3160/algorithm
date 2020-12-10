import sys
input=sys.stdin.readline

n=int(input())
arr=[[0]*n for _ in range(n)]
x,y=0,0
for i in range(n**2):
    if i==0:
        arr[0][n//2]=i+1
        y,x=0,n//2
        continue
    if i%n==0:
        y=0 if y==n-1 else y+1
        arr[y][x]=i+1
        continue
    x=0 if x==n-1 else x+1
    y=n-1 if y==0 else y-1
    arr[y][x]=i+1
for i in arr:
    print(*i)

