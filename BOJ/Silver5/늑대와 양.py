# 16956번
import sys
input=sys.stdin.readline

def func(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<c and 0<=ny<r:
            if arr[ny][nx]=='.':
                arr[ny][nx]='D'
            if arr[ny][nx]=='S':
                return False
    return True

dx=[0,0,1,-1]
dy=[1,-1,0,0]

r,c=map(int,input().split())
arr=[]
for _ in range(r):
    arr.append(list(input().rstrip('\n')))
flag=True
for i in range(r):
    for j in range(c):
        if arr[i][j]=='W':
            flag=func(j,i)
            if not flag:
                break
    else:
        continue
    break
if flag:
    print(1)
    for i in arr:
        print("".join(i))
else:
    print(0)