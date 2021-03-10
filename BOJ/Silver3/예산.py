# 2512번
import sys
input=sys.stdin.readline

n=int(input())
arr=[*map(int,input().split())]
m=int(input())
start=0
end=max(arr)
while start<end:
    mid=(start+end)//2
    k=sum([min(i,mid) for i in arr])
    if k<m:
        start=mid+1
    else:
        end=mid
k=sum([min(i,end) for i in arr])
print(end if k<=m else end-1)