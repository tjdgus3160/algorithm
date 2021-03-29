# 16471번
import sys
input=sys.stdin.readline

n=int(input())
arr=[*map(int,input().split())]
tmp=[*map(int,input().split())]

arr.sort(reverse=True)
tmp.sort(reverse=True)

res=0
idx=0
for i in tmp:
    while idx<n and arr[idx]>=i:
        idx+=1
    if idx==n:
        break
    idx+=1
    res+=1
print('YES' if res>=(n+1)//2 else 'NO')