# 1966번
from collections import deque
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    dq=deque()
    res=0
    n,m=map(int,input().split())
    tmp=[*map(int,input().split())]
    for idx,v in enumerate(tmp):
        dq.append((idx,v))
    tmp.sort()
    while True:
        idx,v=dq.popleft()
        if tmp[-1]==v:
            tmp.pop()
            res+=1
            if idx==m:
                break
        else:
            dq.append((idx,v))
    print(res)