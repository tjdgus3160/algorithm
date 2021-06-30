# 4889번
from collections import deque
import sys
input=sys.stdin.readline

k=1
while True:
    s=input().rstrip()
    if '-' in s:
        break
    arr=deque([])
    for i in s:
        if arr and i=='}' and arr[-1]=='{':
            arr.pop()
        else:
            arr.append(i)
    res=0
    for i in range(0,len(arr),2):
        if arr[i]=='{':
            res+=1
        else:
            if arr[i+1]=='}':
                res+=1
            else:
                res+=2
    print(f'{k}. {res}')
    k+=1