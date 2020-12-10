from collections import deque
import sys
input=sys.stdin.readline

dq=deque()
n=int(input())
for i in range(n):
    s,*r=input().split()
    if 'push' in s:
        dq.append(r[0])
    elif 'top' in s:
        print(dq[-1] if dq else "-1")
    elif 'pop' in s:
        if dq:
            dq.pop()
    elif 'size' in s:
        print(len(dq))
    elif 'empty' in s:
        print("true" if not dq else "false")


