from collections import deque
import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

n=int(input())
dq=deque(["O","X"])
t=1
while t<n:
    k=len(dq)
    for i in range(k):
        tmp=dq.popleft()
        dq.append(tmp+"O")
        dq.append(tmp + "X")
    t+=1
for i in dq:
    print(i)

