# 14499번
import sys
input=sys.stdin.readline

def vaild(nx,ny):
    return 0<=nx<n and 0<=ny<m

dx=[0,0,0,-1,1]
dy=[0,1,-1,0,0]
dice=[0]*7

n,m,x,y,k=map(int,input().split())
board=[[*map(int,input().split())]for _ in range(n)]
dic={1:6,2:5,3:4,4:3,5:2,6:1}
top,east,north=1,3,2

for i in map(int,input().split()):
    nx=x+dx[i]
    ny=y+dy[i]
    if not vaild(nx,ny):
        continue
    if i==1:
        top,east=dic[east],top
    elif i==2:
        top,east=east,dic[top]
    elif i==3:
        top,north=dic[north],top
    else:
        top,north=north,dic[top]
    if not board[nx][ny]:
        board[nx][ny]=dice[dic[top]]
    else:
        dice[dic[top]]=board[nx][ny]
        board[nx][ny]=0
    x,y=nx,ny
    print(dice[top])
