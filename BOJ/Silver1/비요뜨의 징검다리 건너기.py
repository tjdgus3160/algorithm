# 18291번
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

def func(a,b):
    if b==0:
        return 1
    n=func(a,b//2)
    if b%2==0:
        return n*n%1000000007
    else:
        return a*n*n%1000000007

for _ in range(int(input())):
    n=int(input())
    if n<3:
        print(1)
    else:
        print(func(2,n-2)%1000000007)
