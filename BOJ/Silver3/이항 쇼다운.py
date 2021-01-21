# 6591번
from math import factorial
import sys
input=sys.stdin.readline

while True:
    n,k=map(int,input().split())
    if n==0 and k==0:
        break
    if k>n//2:
        k=n-k
    res = 1
    for i in range(n, n - k, -1):
        res *= i
    res //= factorial(k)
    print(res)
