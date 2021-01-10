# 3085번
import sys
input=sys.stdin.readline

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def func(x,y):
    k=arr[y][x]
    r,c=1,1
    ny=y+1
    while ny<n:
        if arr[ny][x]==k:
            c+=1
        else:
            break
        ny+=1
    ny=y-1
    while ny>=0:
        if arr[ny][x]==k:
            c+=1
        else:
            break
        ny-=1
    nx=x+1
    while nx<n:
        if arr[y][nx]==k:
            r+=1
        else:
            break
        nx+=1
    nx=x-1
    while nx>=0:
        if arr[y][nx]==k:
            r+=1
        else:
            break
        nx-=1
    return max(r,c)

def check(x,y):
    cnt=0
    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]
        if 0<=nx<n and 0<=ny<n:
            arr[y][x],arr[ny][nx]=arr[ny][nx],arr[y][x]
            cnt=max(cnt,func(nx,ny))
            arr[y][x],arr[ny][nx]=arr[ny][nx],arr[y][x]
    return cnt

arr=[]
res=0
n=int(input())
for _ in range(n):
    arr.append(list(input().rstrip('\n')))
for i in range(n):
    for j in range(n):
        res=max(res,check(j,i),func(j,i))
print(res)