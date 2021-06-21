# 9626번
import sys
input=sys.stdin.readline

m,n=map(int,input().split())
u,l,r,d=map(int,input().split())
arr=[input().rstrip() for _ in range(m)]
res=[[0]*(l+n+r) for _ in range(u+m+d)]
for y in range(u+m+d):
    for x in range(l+n+r):
        res[y][x]='#' if (x+y)%2==0 else '.'

for y in range(m):
    for x in range(n):
        res[u+y][l+x]=arr[y][x]
for i in res:
    print(''.join(i))
