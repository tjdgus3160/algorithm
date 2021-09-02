# 18115번
from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
dq=deque([*range(1,n+1)])
a=deque()
b=deque()
for i in [*map(int,input().split())][::-1]:
    if i==1:
        if a:
            b.appendleft(a.pop())
        a.append(dq.popleft())
    elif i==2:
        b.appendleft(dq.popleft())
    else:
        b.append(dq.popleft())
print(*(a+b))