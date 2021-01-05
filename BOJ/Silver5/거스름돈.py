# 14916번
import sys
input=sys.stdin.readline

dp=[0,-1,1,-1,2,1]+[0]*100000
for i in range(6,100001):
    if dp[i-5]+1:
        dp[i] = dp[i-5] + 1
    if dp[i]==0 and dp[i-2]+1>0:
        dp[i] = dp[i-2]+1
    elif dp[i-2]+1<dp[i]:
        dp[i] = dp[i - 2] + 1
n=int(input())
print(dp[n])