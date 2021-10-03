# 17142번
from collections import deque
from itertools import combinations
import sys
input=sys.stdin.readline

def bfs(start,cnt):
    for x,y in start:
        lab[x][y]=-1
    time=0
    dq=deque(start)
    while dq and cnt:
        k=len(dq)
        for _ in range(k):
            x,y=dq.popleft()
            for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0<=nx<n and 0<=ny<n and(lab[nx][ny]==2 or not lab[nx][ny]):
                    if not lab[nx][ny]:
                        cnt-=1
                    lab[nx][ny] = -1
                    dq.append((nx, ny))

        time+=1
    return time if not cnt else -1

n,m=map(int,input().split())
board=[]
empty=0
virus = []
for x in range(n):
    tmp=[*map(int,input().split())]
    for y in range(n):
        if tmp[y]==2:
            virus.append((x,y))
        elif not tmp[y]:
            empty+=1
    board.append(tmp)

res=float('inf')
for sub in combinations(virus,m):
    lab=[i[:] for i in board]
    k=bfs(sub,empty)
    if k>=0:
        res=min(res,k)
print(res if res!=float('inf') else -1)