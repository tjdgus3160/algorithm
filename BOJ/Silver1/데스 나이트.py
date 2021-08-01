# 16948번
from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
sy,sx,ey,ex=map(int,input().split())
visited=[[False]*n for _ in range(n)]
visited[sy][sx]=True
dq=deque([[sx,sy]])
res=0
while dq:
    res+=1
    for _ in range(len(dq)):
        c,r=dq.popleft()

        for ny,nx in [(r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)]:
            if 0<=nx<n and 0<=ny<n and not visited[ny][nx]:
                if nx==ex and ny==ey:
                    print(res)
                    exit()
                dq.append([nx,ny])
                visited[ny][nx]=True
print(-1)