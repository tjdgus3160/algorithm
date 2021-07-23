# 14225번
from itertools import combinations
import sys
input=sys.stdin.readline

n=int(input())
arr=[*map(int,input().split())]
tmp=set()
for i in range(2,len(arr)+1):
    for sub in combinations(arr,i):
        tmp.add(sum(sub))
k=1
while k in arr or k in tmp:
    k+=1
print(k)
