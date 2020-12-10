from collections import deque
import sys
input=sys.stdin.readline

dq=deque([0,1,3,5])
n=int(input())
while len(dq)<=n:
    dq.append(2*dq[-2]+dq[-1])
print(dq[n]%100007)
