# 10826번
import sys
sys.setrecursionlimit(10**9)

def fiboDP(n, dp):
    if n <=1:
        return n
    if dp[n] is None:
        dp[n]=fiboDP(n-2,dp)+fiboDP(n-1,dp)
    return dp[n]

n=int(input())
dp=[None]*(n+1)
print(fiboDP(n,dp))