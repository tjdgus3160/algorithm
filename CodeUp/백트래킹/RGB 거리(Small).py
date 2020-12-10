import sys
input=sys.stdin.readline
INF=sys.maxsize

n=int(input())
tmp=[]
for i in range(n):
    tmp.append([*map(int,input().split())])
dp=[[0,0,0] for _ in range(n)]
for i in range(n):
    if i==0:
        dp[i]=tmp[i]
    else:
        dp[i][0]=tmp[i][0]+min(dp[i-1][1],dp[i-1][2])
        dp[i][1]=tmp[i][1]+min(dp[i-1][0],dp[i-1][2])
        dp[i][2]=tmp[i][2]+min(dp[i-1][0],dp[i-1][1])
print(min(dp[-1]))
