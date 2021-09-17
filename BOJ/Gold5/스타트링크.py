# 5014번
from collections import deque
import sys
input=sys.stdin.readline

f,s,g,u,d=map(int,input().split())

visited={s}
dq=deque([(s,0)])
while dq:
    floor,cnt=dq.popleft()
    if floor==g:
        print(cnt)
        exit()
    for v in [floor+u,floor-d]:
        if 1<=v<=f and v not in visited:
            dq.append((v,cnt+1))
            visited.add(v)
print('use the stairs')