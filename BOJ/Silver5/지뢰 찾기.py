# 4396번
import sys
input=sys.stdin.readline

dx=[0,0,1,-1,1,1,-1,-1]
dy=[1,-1,0,0,1,-1,1,-1]

n=int(input())
arr=[]
for _ in range(n):
    arr.append(input().rstrip('\n'))
tmp=[]
for _ in range(n):
    tmp.append(input().rstrip('\n'))
res=[]
for _ in range(n):
    res.append(['.']*n)
flag=False
for y in range(n):
    for x in range(n):
        if tmp[y][x]=='x':
            if arr[y][x]=='.':
                k=0
                for i in range(8):
                    ny=y+dy[i]
                    nx=x+dx[i]
                    if 0<=nx<n and 0<=ny<n and arr[ny][nx]=='*':
                        k+=1
                res[y][x]=str(k)
            elif arr[y][x]=='*':
                flag=True
if flag:
    for y in range(n):
        for x in range(n):
            if arr[y][x]=='*':
                res[y][x]='*'
for i in res:
    print(''.join(i))