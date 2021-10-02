# 2012번
import sys
input=sys.stdin.readline

n=int(input())
rank=[False]*(n+1)
rank[0]=True
arr=[]
for _ in range(n):
    v=int(input())
    if v>n or rank[v]:
        arr.append(v)
    else:
        rank[v]=True
arr.sort()
res=0
idx=0
for i in range(1,n+1):
    if not rank[i]:
        res+=abs(arr[idx]-i)
        idx+=1
print(res)