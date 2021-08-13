import sys
input=sys.stdin.readline

n=int(input())
dp=[0,1,2]
for i in range(3,n+1):
    res=dp[-1]*2
    for j in range(1,i):
        res+=dp[j]*dp[i-j-1]
    dp.append(res)
print(dp[n])