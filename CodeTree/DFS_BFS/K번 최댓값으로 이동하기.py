from collections import deque
import sys
input=sys.stdin.readline

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def check(arr1,arr2):
    if not arr1:
        return arr2
    if arr1[2]!=arr2[2]:
        return arr1 if arr1[2]>arr2[2] else arr2
    if arr1[1]!=arr2[1]:
        return arr1 if arr1[1]<arr2[1] else arr2
    if arr1[0]!=arr2[0]:
        return arr1 if arr1[0]<arr2[0] else arr2
    return arr1

def bfs(x,y):
    visited=[[False]*n for _ in range(n)]
    dq = deque([[x, y]])
    k=arr[y][x]
    visited[y][x]=True
    res=[]
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[ny][nx]<k and not visited[ny][nx]:
                visited[ny][nx]=True
                res=check(res,[nx,ny,arr[ny][nx]])
                dq.append([nx, ny])
    return res

n,k=map(int,input().split())
arr=[[*map(int,input().split())]for _ in range(n)]
sy,sx=map(lambda x:int(x)-1,input().split())
for _ in range(k):
    next=bfs(sx,sy)
    if not next:
        break
    sx,sy=next[0],next[1]
print(sy+1,sx+1)
