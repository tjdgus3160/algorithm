# 14501번
import sys
input=sys.stdin.readline

n=int(input())
dp=[0]*(n+1)
arr=[]
for i in range(n):
    a,b=map(int,input().split())
    if i+a<=n:
        dp[i+a]=max(dp[i+a],(max(dp[:i+1])+b))
print(max(dp))