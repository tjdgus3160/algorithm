# 2343번
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[*map(int,input().split())]
l=max(arr)
r=sum(arr)
while l<=r:
    mid=(l+r)//2
    k=1
    tmp=0
    for i in arr:
        if tmp+i<=mid:
            tmp+=i
        else:
            tmp=i
            k+=1
    if k<=m:
        r=mid-1
    else:
        l=mid+1
print(l)