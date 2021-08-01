# 16236번
from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def find(loc,size):
    visited=[[False]*n for _ in range(n)]
    visited[loc[1]][loc[0]]=True
    dq=deque([loc])
    cnt=1
    while dq:
        tmp = []
        for _ in range(len(dq)):
            x,y=dq.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<n and 0<=ny<n and not visited[ny][nx]:
                    t=arr[ny][nx]
                    if t==0 or t==size:
                        dq.append([nx,ny])
                        visited[ny][nx]=True
                    elif t<size:
                        tmp.append([nx,ny])
        if tmp:
            tmp.sort(key=lambda x:(x[1],x[0]))
            return tmp[0]+[cnt]
        cnt+=1
    return -1

n=int(input())
arr=[]
loc=[]
size=2
k=2
res=0
for i in range(n):
    tmp=[*map(int,input().split())]
    if 9 in tmp:
        loc=[tmp.index(9),i]
    arr.append(tmp)

while True:
    next=find(loc,size)
    if next==-1:
        break
    arr[next[1]][next[0]]=9
    arr[loc[1]][loc[0]]=0
    k-=1
    if not k:
        size+=1
        k=size
    res+=next[2]
    loc=next[:2]
print(res)