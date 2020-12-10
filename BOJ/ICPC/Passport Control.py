# 16288번
from collections import deque
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
arr=[*map(int,input().split())]
q=[0]*k
flag1=True
for i in arr:
    flag2=False
    for j in range(len(q)):
        if q[j]<i:
            q[j]=i
            flag2=True
            break
    if not flag2:
        flag1=False
        break
if flag1:
    print("YES")
else:
    print("NO")