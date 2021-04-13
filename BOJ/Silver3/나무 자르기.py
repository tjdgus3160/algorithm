# 2805번
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[*map(int,input().split())]
start=0
end=max(arr)
res=0
while start<=end:
    mid=(start+end)//2
    k=sum([i-mid for i in arr if i>mid])
    if k<m:
        end=mid-1
    else:
        start=mid+1
print(end)