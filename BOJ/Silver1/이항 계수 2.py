# 11051번
from math import factorial
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
res=1
if k>n//2:
    k=n-k
for i in range(k):
    res*=(n-i)
print((res//factorial(k))%10007)
