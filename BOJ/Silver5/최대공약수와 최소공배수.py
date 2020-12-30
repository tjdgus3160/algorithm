# 2609번
from math import gcd
import sys
input=sys.stdin.readline

a,b=map(int,input().split())
print(gcd(a,b))
print(a*b//gcd(a,b))