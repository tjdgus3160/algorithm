# 16439번
from itertools import combinations
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[[*map(int,input().split())] for _ in range(n)]
res=0
for sub in combinations(range(m),3):
    tmp=0
    for p in arr:
        tmp+=max(p[sub[0]],p[sub[1]],p[sub[2]])
    res=max(res,tmp)
print(res)