# 18870번
from bisect import bisect_left
import sys
input=sys.stdin.readline

n=int(input())
arr=[*map(int,input().split())]
tmp=sorted(list(set(arr)))
res=[]
for i in arr:
    res.append(bisect_left(tmp,i))
print(*res)
