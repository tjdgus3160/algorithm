# 11971번
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[0]*101
loc=0
for _ in range(n):
    a,b=map(int,input().split())
    for i in range(loc+1,loc+a+1):
        arr[i]=b
    loc+=a
loc=0
res=0
for _ in range(m):
    a,b=map(int,input().split())
    for i in range(loc+1,loc+a+1):
        if arr[i]<b and res<b-arr[i]:
            res=b-arr[i]
    loc += a
print(res)