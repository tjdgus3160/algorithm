# 4150번
import sys
input=sys.stdin.readline

dp=[0,1,1]
n=int(input())
for _ in range(3,n+1):
    dp.append(dp[-1]+dp[-2])
print(dp[n])