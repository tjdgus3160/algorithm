from collections import defaultdict,deque
from itertools import permutations

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def vaild(nx,ny):
    return 0<=nx<4 and 0<=ny<4

def jump(nx,ny,i):
    while True:
        if not vaild(nx + dx[i], ny + dy[i]) or board[nx][ny]:
            break
        nx += dx[i]
        ny += dy[i]
    return nx,ny

def bfs(start, end):
    sx, sy = start
    ex, ey = end
    dq = deque([(sx, sy)])
    dist=[[-1]*4 for _ in range(4)]
    dist[sx][sy]=0
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if not vaild(nx,ny):
                continue
            # 그냥 이동
            if dist[nx][ny]==-1 or dist[x][y]+1<dist[nx][ny]:
                dist[nx][ny]=dist[x][y]+1
                dq.append((nx,ny))

            nx,ny=jump(nx,ny,i)
            if dist[nx][ny]==-1 or dist[x][y]+1<dist[nx][ny]:
                dist[nx][ny]=dist[x][y]+1
                dq.append((nx,ny))

    return dist[ex][ey]

board=[]
def solution(arr, r, c):
    global board
    res = float('inf')
    card=defaultdict(list)
    for i in range(4):
        for j in range(4):
            if arr[i][j]:
                card[arr[i][j]].append((i,j))
    for sub in permutations(card.keys()):
        board=[i[:] for i in arr]
        cnt=0
        x,y=r,c
        for i in sub:
            case1=bfs((x,y),card[i][0])
            case2=bfs((x,y),card[i][1])
            if case1<case2:
                cnt+=case1
                cnt+=bfs(card[i][0],card[i][1])
                x,y=card[i][1]
            else:
                cnt+=case2
                cnt+=bfs(card[i][1],card[i][0])
                x,y=card[i][0]
            board[card[i][0][0]][card[i][0][1]]=0
            board[card[i][1][0]][card[i][1][1]]=0
            cnt+=2
        res=min(res,cnt)
    return res

arr=[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r=1
c=0
print(solution(arr,r,c))