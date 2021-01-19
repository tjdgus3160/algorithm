# 1463번
import sys
input=sys.stdin.readline

n=int(input())
dp=[0,0,1,1]+[0]*(n-3)
dp[2],dp[3]=1,1
for i in range(4,n+1):
    tmp=dp[i-1]
    if i%3==0:
        tmp=min(tmp,dp[i//3])
    if i%2==0:
        tmp=min(tmp,dp[i//2])
    dp[i]=tmp+1
print(dp[n])
