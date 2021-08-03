import sys
input=sys.stdin.readline

def check(x,y,i):
    cnt,empty=0,0
    for nx,ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
        if 0<=nx<n and 0<=ny<n:
            if not board[ny][nx]:
                empty+=1
            elif board[ny][nx] in dic[i]:
                cnt+=1
    return cnt,empty

def on_board(i):
    tmp=[]
    for y in range(n):
        for x in range(n):
            if board[y][x]:
                continue
            cnt,empty=check(x,y,i)
            tmp.append([cnt,empty,y,x])
    tmp.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
    board[tmp[0][2]][tmp[0][3]]=i

n=int(input())
board=[[0]*n for _ in range(n)]
dic={}
for _ in range(n*n):
    i,*tmp=map(int,input().split())
    dic[i]=tmp
    on_board(i)
score={0:0,1:1,2:10,3:100,4:1000}
res=0
for y in range(n):
    for x in range(n):
        k,_=check(x,y,board[y][x])
        res+=score[k]
print(res)