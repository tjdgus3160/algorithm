# 1347번
import sys
input=sys.stdin.readline

arr=[['#']*101 for _ in range(101)]
loc=[50,50]
x1,x2,y1,y2=50,50,50,50
arr[loc[1]][loc[0]]='.'
dx=[0,-1,0,1]
dy=[1,0,-1,0]
d=0
input()
for i in input().rstrip():
    if i == 'R':
        d=(d+1)%4
    elif i=='L':
        d=(d+3)%4
    elif i=='F':
        loc[0]+=dx[d]
        loc[1]+=dy[d]
        y1=min(y1,loc[1])
        x2=max(x2,loc[0])
        y2=max(y2,loc[1])
        x1=min(x1,loc[0])
        arr[loc[1]][loc[0]] = '.'

for y in range(y1,y2+1):
    print(''.join(arr[y][x1:x2+1]))