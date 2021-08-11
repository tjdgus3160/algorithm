from collections import deque
import sys
input=sys.stdin.readline

dx=[1,-1,0,0]
dy=[0,0,1,-1]

n,k=map(int,input().split())
arr=[[*map(int,input().split())]for _ in range(n)]
res=0
for _ in range(k):
    y,x=map(lambda x:int(x)-1,input().split())
    if arr[y][x]:
        continue
    arr[y][x]=1
    res+=1
    dq = deque([[x, y]])
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not arr[ny][nx]:
                res+=1
                arr[ny][nx]=1
                dq.append((nx, ny))
print(res)