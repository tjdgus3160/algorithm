# 1145번
from math import gcd
import itertools
import sys
input=sys.stdin.readline

a=[*map(int,input().split())]
res=10**10
for g in list(itertools.combinations(a,3)):
    tmp=g[0]*g[1]//gcd(g[0],g[1])
    res=min(res,tmp*g[2]//gcd(tmp,g[2]))
print(res)