# 2960번
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
arr=[True]*(n+1)
cnt=0
res=0
for i in range(2,n+1):
    if res!=0:
        break
    t=i
    while t<=n:
        if arr[t]:
            arr[t]=False
            cnt+=1
            if cnt==k:
                res=t
                break
        t+=i
print(res)