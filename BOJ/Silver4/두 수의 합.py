# 3273번
import sys
input=sys.stdin.readline

n=int(input())
arr=[*map(int,input().split())]
x=int(input())
arr.sort()
res=0
l=0
r=n-1
while l<r:
    if arr[l]+arr[r]==x:
        res+=1
        l+=1
    elif arr[l]+arr[r]<x:
        l+=1
    else:
        r-=1
print(res)