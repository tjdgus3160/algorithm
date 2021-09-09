# 12100번
from itertools import product
import sys
input=sys.stdin.readline

def rotate(arr):
    n=len(arr)
    tmp=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[i][j] = arr[n-j-1][i]
    return tmp

def tilt(d,board):
    for _ in range(d):
        board=rotate(board)
    tmp=[[0]*n for _ in range(n)]
    for i in range(n):
        idx = 0
        for j in range(n):
            if not board[i][j]: continue
            if not tmp[i][idx]:
                tmp[i][idx]=board[i][j]
            elif board[i][j]==tmp[i][idx]:
                tmp[i][idx]*=2
                idx+=1
            else:
                idx+=1
                tmp[i][idx]=board[i][j]
    for _ in range(4-d):
        tmp = rotate(tmp)
    return tmp

n=int(input())
arr=[[*map(int,input().split())]for _ in range(n)]
res=0
for sub in product(range(4),repeat=5):
    board=[i[:] for i in arr]
    for i in sub:
        board=tilt(i,board)
        res=max(res,max(max(line) for line in board))
print(res)