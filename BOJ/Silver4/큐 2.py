# 18258번
from collections import deque
import sys
input=sys.stdin.readline

dq=deque([])

for _ in range(int(input())):
    cmd=input().rstrip('\n')
    if "push" in cmd:
        s,v=cmd.split()
        dq.append(v)
    elif "pop" in cmd:
        print(dq.popleft() if dq else -1)
    elif "size" in cmd:
        print(len(dq))
    elif "empty" in cmd:
        print(1 if not dq else 0)
    elif "front" in cmd:
        print(dq[0] if dq else -1)
    else:
        print(dq[-1] if dq else -1)