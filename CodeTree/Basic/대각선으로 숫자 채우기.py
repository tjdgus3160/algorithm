n,m=map(int,input().split())
res=[[0]*m for _ in range(n)]
k=1
for x in range(m):
    y=0
    while 0<=x-y and y<n:
        res[y][x-y]=k
        k+=1
        y+=1
for y in range(1,n):
    t=0
    while 0<=m-1-t and y+t<n:
        res[y+t][m-1-t]=k
        k+=1
        t+=1
for i in res:
    print(*i)