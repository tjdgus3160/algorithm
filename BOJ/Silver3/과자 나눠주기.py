# 16401번
import sys
input=sys.stdin.readline

m,n=map(int,input().split())
arr=[*map(int,input().split())]
s,e=1,max(arr)
res=0
while s<=e:
    mid=(s+e)//2
    k=sum([i//mid for i in arr])
    if k>=m:
        res=mid
        s=mid+1
    else:
        e=mid-1
print(res)