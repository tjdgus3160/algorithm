# 1003번
import sys
input=sys.stdin.readline

dp=[[0,0,0] for _ in range(41)]
dp[0]=[0,1,0]
dp[1]=[1,0,1]
for i in range(2,41):
    dp[i][0]=dp[i-1][0]+dp[i-2][0]
    dp[i][1]=dp[i-1][1]+dp[i-2][1]
    dp[i][2]=dp[i-1][2]+dp[i-2][2]
for _ in range(int(input())):
    n=int(input())
    print(dp[n][1],dp[n][2])