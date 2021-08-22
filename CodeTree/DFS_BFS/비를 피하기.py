from collections import deque
import sys
input=sys.stdin.readline

def bfs(x,y):
    visited=set()
    dq=deque([[x,y,0]])
    visited.add((x,y))
    while dq:
        x,y,c=dq.popleft()
        for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if 0<=nx<n and 0<=ny<n and arr[ny][nx]!=1 and (nx,ny) not in visited:
                if arr[ny][nx]==3:
                    return c+1
                visited.add((nx,ny))
                dq.append([nx,ny,c+1])
    return -1

n,h,m=map(int,input().split())
arr=[]
people=[]
for y in range(n):
    tmp=[*map(int,input().split())]
    for x in range(n):
        if tmp[x]==2:
            people.append((x,y))
    arr.append(tmp)

res=[[0]*n for _ in range(n)]
for x,y in people:
    res[y][x]=bfs(x,y)
for i in res:
    print(*i)