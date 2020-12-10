import itertools
import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

dp=[0]
n=int(input())
for i in range(1,n+1):
    if i<3:
        dp.append(1)
    else:
        dp.append(dp[-1]+dp[-2])
print(dp[n])
