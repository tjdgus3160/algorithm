# 9417번
from itertools import combinations
from math import gcd
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    arr=[*map(int,input().split())]
    res=1
    for a,b in combinations(arr,2):
        res=max(res,gcd(a,b))
    print(res)