# 3190번
from collections import deque
import sys
input=sys.stdin.readline

def vaild(nx,ny):
    return 0<=nx<n and 0<=ny<n

dx=[0,1,0,-1] # 우 하 좌 상
dy=[1,0,-1,0]
d=0
n=int(input())
board=[[0]*n for _ in range(n)]
for _ in range(int(input())):
    x,y=map(lambda x:int(x)-1,input().split())
    board[x][y]=2
move=deque()
for _ in range(int(input())):
    t,s=input().split()
    move.append((int(t),s))
res=0
x,y=0,0
board[x][y]=1
dq=deque([(x,y)])
while True:
    res+=1
    nx=x+dx[d]
    ny=y+dy[d]
    if not vaild(nx,ny) or board[nx][ny]==1:
        break
    elif board[nx][ny]==0:
        i,j=dq.popleft()
        board[i][j]=0
    board[nx][ny]=1
    dq.append((nx,ny))
    if move and res==move[0][0]:
        _,s=move.popleft()
        if s=='D':
            d=(d+1)%4
        else:
            d=(d+3)%4
    x,y=nx,ny
print(res)