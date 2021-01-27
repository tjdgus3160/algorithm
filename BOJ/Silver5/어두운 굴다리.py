# 17266번
import math
import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
arr=[*map(int,input().split())]
res=arr[0]-0
for i in range(1,m):
    res=max(res,math.ceil((arr[i]-arr[i-1])/2))
res=max(res,n-arr[-1])
print(res)