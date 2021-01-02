# 2303번
from itertools import combinations
import sys
input=sys.stdin.readline

res=0
cnt=0
for i in range(int(input())):
    k=0
    for sub in combinations(map(int,input().split()),3):
        k=max(k,sum(sub)%10)
    if cnt<=k:
        cnt=k
        res=i+1
print(res)