# 1449번
import sys
input=sys.stdin.readline

n,l=map(int,input().split())
arr=[*map(int,input().split())]
arr.sort()
res=1
flag=False
tmp=arr[0]+l-1
for i in range(n):
    if arr[i]>tmp:
        tmp=arr[i]+l-1
        res+=1
print(res)