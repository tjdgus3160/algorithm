# 18242번
from collections import deque
import sys
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(input().rstrip('\n')))
sx,sy=0,0
for y in range(n):
    for x in range(m):
        if arr[y][x]=='#':
            sx,sy=x,y
            break
    else:
        continue
    break
ex,ey=0,0
for y in range(n-1,-1,-1):
    for x in range(m-1,-1,-1):
        if arr[y][x]=='#':
            ex,ey=x,y
            break
    else:
        continue
    break
flag=True
if '.' in arr[sy][sx:ex+1]:
    print('UP')
    flag=False
if flag and '.' in arr[ey][sx:ex+1]:
    print('DOWN')
    flag=False
if flag:
    for y in range(sy,ey+1):
        if arr[y][sx]=='.':
            print('LEFT')
            flag=False
if flag:
    print("RIGHT")