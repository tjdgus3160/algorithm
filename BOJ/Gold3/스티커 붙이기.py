# 18808번
import sys
input=sys.stdin.readline

def check(r,c,x,y):
    for i in range(r):
        for j in range(c):
            if arr[i][j]+board[i+x][j+y]==2:
                return False
    for i in range(r):
        for j in range(c):
            board[i+x][j+y]+=arr[i][j]
    return True

def rotate(arr):
    r=len(arr)
    c=len(arr[0])
    tmp=[[0]*r for _ in range(c)]
    for i in range(c):
        for j in range(r):
            tmp[i][j]=arr[r-1-j][i]
    return tmp

n,m,k=map(int,input().split())
board=[[0]*m for _ in range(n)]
for _ in range(k):
    r,c=map(int,input().split())
    arr=[[*map(int,input().split())]for _ in range(r)]
    for _ in range(4):
        flag=False
        for x in range(n-r+1):
            for y in range(m-c+1):
                if check(r,c,x,y):
                    flag=True
                    break
            else:
                continue
            break
        if flag:
            break
        arr=rotate(arr)
        r,c=c,r
print(sum([i.count(1) for i in board]))
