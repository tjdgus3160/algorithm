# 2567번
import sys
input=sys.stdin.readline

dx=[0,0,-1,1]
dy=[1,-1,0,0]

arr=[[0]*100 for _ in range(100)]
res=0
for _ in range(int(input())):
    x,y=map(int,input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            if arr[i][j]:
                continue
            arr[i][j]=1
            if res==0:
                res+=4
            else:
                k=0
                for d in range(4):
                    nx=j+dx[d]
                    ny=i+dy[d]
                    if 0<=nx<100 and 0<=ny<100 and arr[ny][nx]:
                        k+=1
                res=res+4-2*k
print(res)