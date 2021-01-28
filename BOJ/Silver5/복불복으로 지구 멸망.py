# 17358번
from itertools import permutations
import sys
input=sys.stdin.readline

n=int(input())
if n==2:
    print(1)
else:
    res=1
    k=2
    while k<n:
        k+=2
        res=(k-1)*res
    print(res%(10**9+7))