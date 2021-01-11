# 5347번
from math import gcd
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    a,b=map(int,input().split())
    print(a*b//gcd(a,b))