# 2714번
from collections import deque
import sys
input=sys.stdin.readline

dx=[0,1,0,-1]
dy=[-1,0,1,0]

ans=[]
alp={0:' '}
for i in range(1,27):
    alp[i]=chr(ord('A')+i-1)
for _ in range(int(input())):
    r,c,s=input().split()
    r,c=int(r),int(c)
    arr=deque([list(s[i:i+c]) for i in range(0, len(s),c)])
    tmp=""
    res = ""
    d = 1  # 상0 우1 하2 좌3
    cnt=0
    x,y=0,0
    total=r*c-r*c%5
    while cnt < total:
        tmp+=arr[y][x]
        if len(tmp)==5:
            res+=alp[int(tmp,2)]
            tmp=""
        arr[y][x]=-1
        if d == 0 and (y==0 or arr[y-1][x]==-1):
            d = 1
        elif d == 1 and (x==c-1 or arr[y][x+1]==-1):
            d = 2
        elif d == 2 and (y==r-1 or arr[y+1][x]==-1):
            d = 3
        elif d == 3 and (x==0 or arr[y][x-1]==-1):
            d = 0
        y,x=y+dy[d],x+dx[d]
        cnt+=1
    while len(res)>1 and res[-1]==' ':
        res=res.rstrip(' ')
    print(res)