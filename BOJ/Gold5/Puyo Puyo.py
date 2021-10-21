# 11559번
from collections import deque
import sys
input=sys.stdin.readline

def bfs(x,y,c):
    tmp=[(x,y)]
    dq=deque([(x,y)])
    while dq:
        x,y=dq.popleft()
        for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if 0<=nx<12 and 0<=ny<6 and board[nx][ny]==c and (nx,ny) not in tmp:
                tmp.append((nx,ny))
                dq.append((nx,ny))
    if len(tmp)>3:
        checked.extend(tmp)

board=[list(input().rstrip())for _ in range(12)]
res=0
while True:
    checked=[]
    for x in range(12):
        for y in range(6):
            if board[x][y]!='.' and (x,y) not in checked:
                bfs(x,y,board[x][y])
    if not checked:
        break
    for x,y in checked:
        board[x][y]='.'
    for y in range(6):
            t = 11
            for x in range(11,-1,-1):
                if board[x][y]=='.':
                    continue
                if board[x][y]!='.' and x!=t:
                    board[t][y]=board[x][y]
                    board[x][y]='.'
                t-=1
    res+=1
print(res)