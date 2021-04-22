# 8911번
import sys
input=sys.stdin.readline

# 시계방향 0,1,2,3
dx=[0,1,0,-1]
dy=[1,0,-1,0]

for _ in range(int(input())):
    s=input().rstrip()
    d=0
    x,y=500,500
    X,Y=[500,500],[500,500]

    for i in s:
        if i=='F':
            x+=dx[d]
            y+=dy[d]
        elif i=='B':
            x -= dx[d]
            y -= dy[d]
        elif i=='R':
            d=(d+1)%4
        else:
            d=(d-1)%4
        X=[max(x,X[0]),min(x,X[1])]
        Y=[max(y,Y[0]),min(y,Y[1])]
    print((X[0]-X[1])*(Y[0]-Y[1]))