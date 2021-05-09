# 14562번
from collections import deque
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    s,t=map(int,input().split())
    dq=deque([[s,t,0]])
    while dq:
        s,t,k=dq.popleft()
        if s==t:
            print(k)
            break
        if 2*s<=t+3:
            dq.append([2*s,t+3,k+1])
        if s+1<=t:
            dq.append([s+1,t,k+1])
