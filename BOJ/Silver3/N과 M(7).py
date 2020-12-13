# 15656번
import sys
input=sys.stdin.readline

def func(k):
    if k==m:
        print(*arr[:-1])
        return
    for i in range(1,n+1):
        if isused[i]!=0:
            arr[k]=num[i-1]
            isused[i]-=1
            func(k+1)
            isused[i]+=1

n,m=map(int,input().split())
num=[*map(int,input().split())]
num.sort()
arr=[0]*(m+1)
isused=[m]*(n+1)
func(0)