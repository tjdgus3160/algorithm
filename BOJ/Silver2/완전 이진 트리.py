# 9934번
from collections import deque
import sys
input=sys.stdin.readline

k=int(input())
arr=[*map(int,input().split())]
dq=deque([arr])

for _ in range(k):
    tmp=[]
    for _ in range(len(dq)):
        k=dq.popleft()
        mid=len(k)//2
        tmp.append(k[mid])
        if len(k)>1:
            dq.append(k[:mid])
            dq.append(k[mid+1:])
    print(*tmp)