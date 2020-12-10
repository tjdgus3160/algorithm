from collections import deque
import sys
input=sys.stdin.readline

dq=deque([1,2,3])
n=int(input())
while len(dq)<n:
    dq.append(dq[-1]+dq[-2])
print(dq[n-1]%100000007)
