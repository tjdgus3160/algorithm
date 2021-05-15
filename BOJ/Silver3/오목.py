# 2615번
import sys
input=sys.stdin.readline

def check(x,y):
    # 가로 탐색
    cnt=1
    xx=x+1
    while xx<19 and arr[y][xx]==arr[y][x]:
        xx+=1
        cnt+=1
    if cnt==5 and ((x - 1 >= 0 and arr[y][x - 1] != arr[y][x])or(x==0)):
        return True
    # 세로 탐색
    cnt=1
    yy=y+1
    while yy<19 and arr[yy][x]==arr[y][x]:
        yy+=1
        cnt+=1
    if cnt==5 and ((y-1>=0 and arr[y-1][x]!=arr[y][x])or(y==0)):
        return True
    cnt=1
    yy=y-1
    xx=x+1
    while 0<=yy and xx<19 and arr[yy][xx]==arr[y][x]:
        yy-=1
        xx+=1
        cnt+=1
    if cnt==5 and ((x - 1 >= 0 and y + 1 < 19 and arr[y + 1][x - 1] != arr[y][x])or(y==18 or x==0)):
        return True
    cnt=1
    yy=y+1
    xx=x+1
    while yy<19 and xx<19 and arr[yy][xx]==arr[y][x]:
        yy+=1
        xx+=1
        cnt+=1
    if cnt==5 and ((x - 1 >= 0 and y - 1 >= 0 and arr[y - 1][x - 1] != arr[y][x])or(y==0 or x==0)):
        return True
    return False

arr=[[*map(int,input().split())] for _ in range(19)]
flag=True
for y in range(19):
    for x in range(19):
        if arr[y][x] and check(x,y):
            flag=False
            print(arr[y][x])
            print(y+1,x+1)
            break
    else:
        continue
    break
if flag:
    print(0)

