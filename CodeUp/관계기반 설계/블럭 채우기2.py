from collections import deque
import sys
input=sys.stdin.readline

dq=deque([0,0,0,2,0,0,4])
n=int(input())
while len(dq)<=n:
    dq.append(2*dq[-3])
print(dq[n]%100000007)
