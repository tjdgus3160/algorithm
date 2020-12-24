# 1038번
from _collections import deque
import sys
input=sys.stdin.readline

n=int(input())
arr=[0,1,2,3,4,5,6,7,8,9,10]
cnt=10
if n>10:
    dq = deque(arr[2:])
    while dq:
        t=dq.popleft()
        for i in range(t%10):
            k=t*10+i
            dq.append(k)
            arr.append(k)
            cnt+=1
print(arr[n] if n<len(arr) else -1)