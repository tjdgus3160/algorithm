# 17626번
from bisect import bisect_left
import sys
input=sys.stdin.readline

arr=[i*i for i in range(1,224)]
dp=[float('inf')]*50001
for i in range(1,50001):
    if i in arr:
        dp[i]=1
        continue
    k=bisect_left(arr,i)
    for j in arr[:k]:
        dp[i]=min(dp[i],dp[i-j]+1)
print(dp[int(input())])
