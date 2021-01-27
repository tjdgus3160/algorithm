# 2428번
import sys
input=sys.stdin.readline

def bi(v):
    start=v
    end=n
    while start<end:
        mid=(start+end)//2
        if arr[mid]*0.9 <= arr[v]:
            start=mid+1
        else:
            end=mid
    return end-1

n=int(input())
arr=[*map(int,input().split())]
arr.sort()
res=0
for i in range(n-1):
    res+=bi(i)-i
print(res)