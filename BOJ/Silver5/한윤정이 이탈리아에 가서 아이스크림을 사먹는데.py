# 2422번
from itertools import combinations
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
x=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    x[a][b]=1
    x[b][a]=1
res=0
for a,b,c in combinations(range(1,n+1),3):
    if x[a][b] or x[b][c] or x[c][a]:
        continue
    res+=1
print(res)