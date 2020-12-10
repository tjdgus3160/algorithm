# 1544번
from collections import deque
import sys
input=sys.stdin.readline

dq=deque()
res=[]
for _ in range(int(input())):
    s=list(input())
    if s[-1]=='\n':
        del s[-1]
    s="".join(s)
    dq.append(s)
while dq:
    tmp=deque(list(dq[0]))
    res.append(dq[0])
    for i in range(len(tmp)):
        tmp.rotate(-1)
        while "".join(tmp) in dq:
            dq.remove("".join(tmp))
print(len(res))