# 2748번
import sys
input=sys.stdin.readline

dp=[0]*91
dp[1],dp[2]=1,1
for i in range(3,91):
    dp[i]=dp[i-1]+dp[i-2]
n=int(input())
print(dp[n])
