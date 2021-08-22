from itertools import combinations
from collections import deque
import sys
input=sys.stdin.readline

def bfs(sx,sy,ex,ey):
    global res
    visited=set()
    visited.add((sx,sy))
    dq=deque([[sx,sy,0]])
    while dq:
        x,y,c=dq.popleft()
        for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if 0<=nx<n and 0<=ny<n and not arr[ny][nx] and (nx,ny) not in visited:
                if nx==ex and ny==ey:
                    res=min(res,c+1)
                    return
                visited.add((nx,ny))
                dq.append([nx,ny,c+1])


n,k=map(int,input().split())
arr=[]
wall=[]
for y in range(n):
    tmp=[*map(int,input().split())]
    for x in range(len(tmp)):
        if tmp[x]:
            wall.append((x,y))
    arr.append(tmp)

sy,sx=map(lambda x:int(x)-1,input().split())
ey,ex=map(lambda x:int(x)-1,input().split())
res=float('inf')
for sub in combinations(wall,k):
    for x,y in sub:
        arr[y][x]=0
    bfs(sx,sy,ex,ey)
    for x,y in sub:
        arr[y][x]=1
print(res if res!=float('inf') else -1)