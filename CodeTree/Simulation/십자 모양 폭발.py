n=int(input())
arr=[[*map(int,input().split())] for _ in range(n)]
r,c=map(int,input().split())
r-=1
c-=1
k=arr[r][c]-1
arr[r][c]=0
up,down,left,right=1,1,1,1
while r-up>=0 and up<=k:
    arr[r-up][c]=0
    up+=1
while r+down<n and down<=k:
    arr[r+down][c]=0
    down+=1
while c-left>=0 and left<=k:
    arr[r][c-left]=0
    left+=1
while c+right<n and right<=k:
    arr[r][c+right]=0
    right+=1
tmp=[[0]*n for _ in range(n)]
for x in range(n):
    k=n-1
    for y in range(n-1,-1,-1):
        if arr[y][x]:
            tmp[k][x]=arr[y][x]
            k-=1
for i in tmp:
    print(*i)