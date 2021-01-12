# 11866번
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
arr=[*range(1,n+1)]
res=[]
t=k-1
while arr:
    while t>=len(arr):
        t-=len(arr)
    res.append(arr.pop(t))
    t+=(k-1)
print('<',end='')
for i in range(n):
    if i == n-1:
        print(res[i], end='>')
    else:
        print(res[i], end=', ')