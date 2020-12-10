from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
dq=deque()
res=0
for i in range(n):
    p=int(input())
    if not dq:
        dq.append(p)
        continue
    while dq and dq[-1]<=p:
        dq.pop()
    res+=len(dq)
    dq.append(p)
print(res)

