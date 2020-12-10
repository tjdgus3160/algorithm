# 11727번
import sys
sys.setrecursionlimit(2000)
def find(n):
    if n ==1:
        return 1
    if n==2:
        return 3
    if dp[n] is None:
        dp[n]=find(n-1)+find(n-2)*2
    return dp[n]

dp=[None]*1001
n=int(input())
print(find(n)%10007)