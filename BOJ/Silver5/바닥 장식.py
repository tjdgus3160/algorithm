# 1388번
import sys
input=sys.stdin.readline

def bfs(x,y):
    if arr[y][x]=='|':
        k=y
        while k<n and arr[k][x]=='|':
            arr[k][x]='.'
            k+=1
    elif arr[y][x]=='-':
        k=x
        while k<m and arr[y][k]=='-':
            arr[y][k] = '.'
            k += 1

n,m=map(int,input().split())
arr=[list(input().rstrip()) for _ in range(n)]
res=0
for y in range(n):
    for x in range(m):
        if arr[y][x]!='.':
            bfs(x,y)
            res+=1
print(res)