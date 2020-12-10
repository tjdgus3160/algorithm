# 1436번

import sys
input=sys.stdin.readline

dp=[]
i=666
while len(dp)<10000:
    if '666' in str(i):
        dp.append(i)
    i+=1
n=int(input())
print(dp[n-1])