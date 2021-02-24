import sys
sys.setrecursionlimit(10**9)

def solution(n):
    if n%2==1 or n==0:
        return 0
    dp=[0]*(5001)
    dp[2]=3
    for i in range(4,n+1,2):
        dp[i]=dp[i-2]*3+2*(1+sum(dp[:i-3]))
    return dp[n]%1000000007