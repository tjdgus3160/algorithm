from collections import deque
import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
INF=sys.maxsize

n=int(input())
a=[1,1,2]
b=[1,2,3]
for i in range(3,n):
    a.append(a[-1]+a[-2])
    b.append(a[-1] + a[-2])
print(a[n-1]+b[n-1])
