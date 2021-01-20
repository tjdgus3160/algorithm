# 1874번
from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
dq = deque()
k=1
res = ""
flag=False
for _ in range(n):
    v=int(input())
    if flag:
        continue
    if not dq:
        for i in range(k,v):
            dq.append(i)
            res+='+'
        res += '+'
        res+='-'
        k=v+1
    else:
        if v==dq[-1]:
            res+='-'
            dq.pop()
        elif v>dq[-1] and v>=k:
            for i in range(k, v):
                dq.append(i)
                res+='+'
            res+='+'
            res += '-'
            k = v+1
        else:
            flag=True
if flag:
    print('NO')
else:
    for i in res:
        print(i)