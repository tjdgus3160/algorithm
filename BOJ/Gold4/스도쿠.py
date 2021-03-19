# 2580번
import sys
input=sys.stdin.readline

def func(k):
    if k== len(loc):
        for i in arr:
            print(*i)
        exit()
    x,y=loc[k][0],loc[k][1]
    for i in range(1,10):
        if lineX[x][i] and lineY[y][i] and sqar[3*(y//3)+x//3][i]:
            lineX[x][i]=False
            lineY[y][i]=False
            sqar[3*(y//3)+x//3][i]=False
            arr[y][x]=i
            func(k+1)
            arr[y][x]=0
            lineX[x][i]=True
            lineY[y][i]=True
            sqar[3*(y//3)+x//3][i]=True

arr=[]
for _ in range(9):
    arr.append([*map(int,input().split())])

lineX = [[True]*10 for _ in range(9)]
lineY = [[True]*10 for _ in range(9)]
sqar = [[True]*10 for _ in range(9)]

loc=[]
for y in range(9):
    for x in range(9):
        if arr[y][x]:
            lineY[y][arr[y][x]]=False
            lineX[x][arr[y][x]]=False
            sqar[3*(y//3)+x//3][arr[y][x]]=False
        else:
            loc.append([x,y])
func(0)
