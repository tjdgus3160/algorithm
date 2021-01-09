# 1940번
from collections import deque
import sys
input=sys.stdin.readline

dq=deque([*range(1,int(input())+1)])
while len(dq)>1:
    dq.popleft()
    if len(dq)==1:
        break
    dq.append(dq.popleft())
print(*dq)