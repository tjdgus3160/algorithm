# 16953번
from collections import deque
import sys
input=sys.stdin.readline

a,b=map(int,input().split())
dq=deque([a])
res=0
while dq:
    res+=1
    for _ in range(len(dq)):
        n=dq.popleft()
        if n==b:
            print(res)
            exit()
        if 2*n<=b:
            dq.append(2*n)
        if 10*n+1<=b:
            dq.append(10*n+1)
print(-1)