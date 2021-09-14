# 14891번
from collections import deque
import sys
input=sys.stdin.readline

arr=[deque([*map(int,input().rstrip())]) for _ in range(4)]
for _ in range(int(input())):
    idx,v=map(int,input().split())
    idx-=1
    tmp=[0]*4
    tmp[idx]=v
    for i in range(idx,0,-1):
        if arr[i][6]+arr[i-1][2]==1:
            tmp[i-1]=-1 if tmp[i]==1 else 1
        else:
            break
    for i in range(idx,3):
        if arr[i][2]+arr[i+1][6]==1:
            tmp[i+1]=-1 if tmp[i]==1 else 1
        else:
            break
    for i in range(4):
        if tmp[i]:
            arr[i].rotate(tmp[i])
res=''.join([str(i[0]) for i in arr[::-1]])
print(int(res,2))