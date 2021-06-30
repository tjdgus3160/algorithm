# 13567번
import sys
input=sys.stdin.readline

def move(v,d):
    if di[d]=='u':
        loc[1]+=v
    if di[d]=='d':
        loc[1]-=v
    if di[d]=='r':
        loc[0]+=v
    if di[d]=='l':
        loc[0]-=v
    if not(0<=loc[0]<=m and 0<=loc[1]<=m):
        print(-1)
        exit()

m,n=map(int,input().split())
loc=[0,0]
di=['u','r','d','l']
d=1
for _ in range(n):
    cmd,v=input().split()
    if cmd=='MOVE':
        move(int(v),d)
    else:
        if v=='0':
            d=(d+4-1)%4
        else:
            d=(d+1)%4
print(*loc)