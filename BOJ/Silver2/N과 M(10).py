# 15664번
from collections import Counter
import sys
input=sys.stdin.readline

def func(k):
    if k==m:
        print(*arr[:-1])
        return
    for i in isused:
        if arr[k-1]<=i and isused[i]!=0:
            arr[k]=i
            isused[i]-=1
            func(k+1)
            isused[i]+=1

n,m=map(int,input().split())
num=[*map(int,input().split())]
num.sort()
arr=[0]*(m+1)
isused=Counter(num)
func(0)