# 10866번
from collections import deque
import sys
input=sys.stdin.readline

dq=deque([])
for _ in range(int(input())):
    cmd=input().rstrip('\n')
    if "push" in cmd:
        s,v=cmd.split()
        dq.append(v) if "back" in s else dq.appendleft(v)
    elif "pop" in cmd:
        if "back" in cmd:
            print(dq.pop() if dq else -1)
        else:
            print(dq.popleft() if dq else -1)
    elif "size" in cmd:
        print(len(dq))
    elif "empty" in cmd:
        print(1 if not dq else 0)
    elif "front" in cmd:
        print(dq[0] if dq else -1)
    else:
        print(dq[-1] if dq else -1)