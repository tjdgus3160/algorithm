# 15649번
import sys
input=sys.stdin.readline

def func(k):
    if k==m:
        print(*arr[:-1])
        return
    for i in range(1,n+1):
        if not isused[i]:
            arr[k]=i
            isused[i]=True
            func(k+1)
            isused[i]=False

n,m=map(int,input().split())
arr=[0]*(m+1)
isused=[False]*(n+1)
func(0)