# 1094번
from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
a=deque([64])
while sum(a)>n:
    t=a.popleft()
    a.appendleft(t//2)
    if sum(a)<n:
        a.appendleft(t // 2)
print(len(a))