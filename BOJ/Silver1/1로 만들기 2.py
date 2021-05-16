# 12852번
import sys
input=sys.stdin.readline

n=int(input())
dp=[0,0,1,1,2]+[float('inf')]*(n-4)
parent=[0,0,1,1,2]+[float('inf')]*(n-4)
for i in range(5,n+1):
    if i%3==0:
        dp[i]=dp[i//3]+1
        parent[i]=i//3
    if i%2==0 and dp[i]>(dp[i//2]+1):
        dp[i]=dp[i//2]+1
        parent[i]=i//2
    if dp[i]>dp[i-1]+1:
        dp[i]=dp[i-1]+1
        parent[i]=i-1
res=[n]
while res[-1]!=1:
    res.append(parent[res[-1]])
print(dp[n])
print(*res)
