from itertools import combinations
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[*map(int,input().split())]
res=0
for sub in combinations(arr,m):
    k=0
    for i in sub:
        k=k^i
    res=max(res,k)
print(res)