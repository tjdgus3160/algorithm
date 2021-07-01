# 14503번
import sys
import time

input=sys.stdin.readline

n,m=map(int,input().split())
c,r,d=map(int,input().split())
arr=[[*map(int,input().split())] for _ in range(n)]

dx=[0,1,0,-1]
dy=[-1,0,1,0]

res=0
k=0
while True:
    if not arr[c][r]:
        arr[c][r]=2
        res+=1
    # print(r,c,d)
    if k<4:
        d=(d+3)%4
        k+=1
        if not arr[c+dy[d]][r+dx[d]]:
            c+=dy[d]
            r+=dx[d]
            k=0
    else:
        if arr[c + dy[(d + 2) % 4]][r + dx[(d + 2) % 4]]==1:
            break
        else:
            c += dy[(d + 2) % 4]
            r += dx[(d + 2) % 4]
            k = 0
    # for i in arr:
    #     print(*i)
    # print()
    # time.sleep(1)
print(res)