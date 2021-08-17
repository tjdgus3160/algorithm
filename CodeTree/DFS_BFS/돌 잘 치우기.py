from itertools import combinations
from collections import deque
import sys
input=sys.stdin.readline

def bfs(start):
    dq=deque(start)
    visited=[[False]*n for _ in range(n)]
    for y,x in start:
        visited[y][x]=True
    cnt=len(start)
    while dq:
        y,x=dq.popleft()
        for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if 0<=nx<n and 0<=ny<n and not visited[ny][nx] and not arr[ny][nx]:
                visited[ny][nx]=True
                cnt+=1
                dq.append((ny,nx))
    return cnt

n,k,m=map(int,input().split())
arr=[]
rock=[]
for y in range(n):
    tmp=[*map(int,input().split())]
    for x in range(n):
        if tmp[x]:
            rock.append((x,y))
    arr.append(tmp)
start=[[*map(lambda x:int(x)-1,input().split())]for _ in range(k)]

res=0
for sub in combinations(rock,m):
    for x,y in sub:
        arr[y][x]=0
    res=max(res,bfs(start))
    for x,y in sub:
        arr[y][x]=1
print(res)