from collections import deque
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
arr=[]
empty=[]
start=[]
for y in range(n):
    tmp=[*map(int,input().split())]
    for x in range(n):
        if not tmp[x]:
            empty.append((x,y))
        elif tmp[x]==2:
            start.append([x,y])
    arr.append(tmp)

res=[[-2]*n for _ in range(n)]
for x,y in start:
    res[y][x]=0
dq=deque(start)
while dq:
    x,y=dq.popleft()
    for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if 0<=nx<n and 0<=ny<n and arr[ny][nx] and res[ny][nx]==-2:
            res[ny][nx]=res[y][x]+1
            dq.append([nx,ny])
for x,y in empty:
    res[y][x]=-1
for i in res:
    print(*i)