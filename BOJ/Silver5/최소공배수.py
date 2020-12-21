# 1934번
import sys
from math import gcd
input=sys.stdin.readline

for _ in range(int(input())):
    a,b=map(int,input().split())
    print(a*b//gcd(a,b))