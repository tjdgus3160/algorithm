# 14248번
from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
arr=[*map(int,input().split())]
start=int(input())-1
res=1
dq=deque([start])
dic={start}
while dq:
    k=dq.popleft()
    if 0<=k+arr[k]<n and k+arr[k] not in dic:
        res+=1
        dq.append(k+arr[k])
        dic.add(k+arr[k])
    if 0<=k-arr[k]<n and k-arr[k] not in dic:
        res+=1
        dq.append(k-arr[k])
        dic.add(k-arr[k])
print(res)