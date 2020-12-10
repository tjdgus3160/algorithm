import sys
input=sys.stdin.readline
INF=sys.maxsize

n=int(input())
dp=[0,1,2,3]
for _ in range(n-len(dp)+1):
    dp.append(dp[-1]+dp[-2])
print(dp[n])

