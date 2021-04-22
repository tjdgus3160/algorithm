# 14490번
from math import gcd
import sys
input=sys.stdin.readline

a,b=map(int,input().split(':'))
k=gcd(a,b)
print(f'{a//k}:{b//k}')