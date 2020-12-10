import itertools
import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

k=int(input())
n=int(input())
a=[*map(int,input().split())]
res=0
for i in range(1,n+1):
    tmp=itertools.combinations(a,i)
    for j in tmp:
        if sum(j)>res and sum(j)<k:
            res=sum(j)

print(res)
