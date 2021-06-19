# 18429번
import sys
input=sys.stdin.readline

def func(idx,cur):
    global res
    if idx==n:
        res+=1
        return
    for i in range(n):
        if not used[i] and cur-k+arr[i]>=0:
            used[i]=True
            func(idx+1,cur-k+arr[i])
            used[i]=False

n,k=map(int,input().split())
arr=[*map(int,input().split())]
used=[False]*n
res=0
for i in range(n):
    if arr[i]>=k:
        used[i]=True
        func(1,-k+arr[i])
        used[i]=False
print(res)