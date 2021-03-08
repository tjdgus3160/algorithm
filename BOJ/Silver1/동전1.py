# 2293번
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))

dp=[0]*10001
dp[0]=1
for i in arr:
    for j in range(1,k+1):
        if j>=i:
            dp[j]+=dp[j-i]
print(dp[k])