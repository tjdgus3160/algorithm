# 2133번
def find(n):
    if n%2==1 or n==0:
        return 0
    if n ==2:
        dp[n]=3
        return 3
    if dp[n] ==0:
        dp[n]=find(n-2)*3+2*(sum(dp[:n-3]))
    return dp[n]

dp=[0]*31
dp[0] = 1
n=int(input())
print(find(n))