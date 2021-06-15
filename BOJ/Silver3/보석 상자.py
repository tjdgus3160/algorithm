# 2792번
import math
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[]
for _ in range(m):
    arr.append(int(input()))
s,e=1,max(arr)
res=0
while s<=e:
    mid=(s+e)//2
    k=sum([math.ceil(i/mid) for i in arr])
    if k<=n:
        e=mid-1
    else:
        s=mid+1
print(e+1)