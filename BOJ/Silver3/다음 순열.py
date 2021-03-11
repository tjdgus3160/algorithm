# 10972번
from itertools import permutations
import sys
input=sys.stdin.readline

n=int(input())
arr=[*map(int,input().split())]
if sorted(arr,reverse=True) == arr:
    print(-1)
    exit()
for i in range(n-1,0,-1):
    if arr[i]>arr[i-1]:
        k=arr[i-1]
        tmp=sorted(arr[i-1:])
        idx=tmp.index(k)+1
        res=arr[:i-1]+[tmp[idx]]+tmp[:idx]+tmp[idx+1:]
        print(*res)
        break