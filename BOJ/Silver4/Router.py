# 15828번
from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
dq=deque()
while True:
    v=int(input())
    if v==-1:
        break
    elif v==0:
        dq.popleft()
    elif v>0 and len(dq)<n:
        dq.append(v)
print(*dq if dq else 'empty')