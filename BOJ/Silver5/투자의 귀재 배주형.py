# 19947번
from collections import deque
import sys
input=sys.stdin.readline

h,y=map(int,input().split())
dq=deque([[h,0]])
res=0
while dq:
    h,t=dq.popleft()
    res=max(res,h)
    if t==y:
        continue
    if t+1<=y:
        dq.append([int(h*1.05),t+1])
    if t+3<=y:
        dq.append([int(h*1.2),t+3])
    if t+5<=y:
        dq.append([int(h*1.35),t+5])
print(res)