import sys
from math import gcd
input=sys.stdin.readline

a=[[0]*2000 for _ in range(2000)]
n,m=map(int,input().split())

res=0
for i in range(n,m+1):
    for j in range(i):
        t=gcd(i,j)
        if a[i//t][j//t]==0:
            a[i//t][j//t]=1
            res+=1
print(res)
