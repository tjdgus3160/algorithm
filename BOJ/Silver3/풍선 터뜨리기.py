# 2346번
from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
arr=[*map(int,input().split())]
dq=deque()
for idx,v in enumerate(arr):
    dq.append((idx+1,v))
res=[]
while dq:
    idx,v=dq.popleft()
    res.append(idx)
    if len(dq) == 1:
        break
    if v>0:
        v-=1

        while v:
            dq.append(dq.popleft())
            v-=1
    else:
        while v<0:
            dq.appendleft(dq.pop())
            v+=1
idx, v = dq.popleft()
res.append(idx)
print(*res)