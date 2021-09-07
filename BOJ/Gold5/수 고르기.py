# 2230번
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=sorted([int(input()) for _ in range(n)])
res=float('inf')
cur=0
for idx,v in enumerate(arr):
    if not idx: continue
    if v-arr[cur]>=m:
        res=min(res,v-arr[cur])
        while cur<idx and v-arr[cur]>=m:
            cur+=1
print(res)
