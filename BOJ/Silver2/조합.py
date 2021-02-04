# 2407번
from math import factorial
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
if m>n//2:
    m=n-m
res=1
for i in range(m):
    res*=(n-i)
print(res//factorial(m))