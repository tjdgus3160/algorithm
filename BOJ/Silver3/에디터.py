# 1406번
from collections import deque
import sys
input=sys.stdin.readline

s=list(input().rstrip('\n'))
arr1=deque(s)
arr2=deque()
for _ in range(int(input())):
    i,*v=input().split()
    if i=='L':
        if arr1:
            arr2.appendleft(arr1.pop())
    elif i=='D':
        if arr2:
            arr1.append(arr2.popleft())
    elif i=='B':
        if arr1:
            arr1.pop()
    else:
        arr1.append(v[0])
print(''.join(arr1+arr2))