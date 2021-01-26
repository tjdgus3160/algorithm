# 5568번
from itertools import permutations
import sys
input=sys.stdin.readline

n=int(input())
k=int(input())
arr=[]
for _ in range(n):
    arr.append(input().rstrip('\n'))
res=[]
for sub in permutations(arr,k):
    v="".join(sub)
    if v not in res:
        res.append(v)
print(len(res))