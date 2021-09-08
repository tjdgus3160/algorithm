# 15661번
from itertools import combinations
import sys
input=sys.stdin.readline

def func(group):
    k=0
    for i in group:
        for j in group:
            k+=arr[i][j]
    return k

n=int(input())
arr=[[*map(int,input().split())]for _ in range(n)]

res=float('inf')
for i in range(1,n//2+1):
    for link in combinations(range(n),i):
        start=tuple({*range(n)}-set(link))
        res=min(res,abs(func(link)-func(start)))
print(res)