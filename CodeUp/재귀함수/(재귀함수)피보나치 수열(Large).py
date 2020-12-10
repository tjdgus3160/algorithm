from math import factorial
import sys
input=sys.stdin.readline

def find(n):
    global dp
    if len(dp)>=n+1:
        return dp[n]
    else:
        dp.append(dp[-1]+dp[-2])
    find(n)

n=int(input())
dp=[0,1]
find(n)
print(dp[n]%10009)



