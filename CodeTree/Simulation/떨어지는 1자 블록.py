n,m,k=map(int,input().split())
arr=[[*map(int,input().split())] for _ in range(n)]
s=k-1
e=s+m-1
k=0
for y in range(n):
    for x in range(s,e+1):
        if arr[y][x]:
            break
    else:
        k=y
        continue
    break
for i in range(m):
    arr[k][s+i]=1
for i in arr:
    print(*i)