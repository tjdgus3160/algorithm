# 14465번
import sys
input=sys.stdin.readline

n,k,b=map(int,input().split())
arr=[True]*n
for _ in range(b):
    v=int(input())
    arr[v-1]=False
left=0
right=k-1
res=arr[:k].count(False)
cur=res
for _ in range(n-k):
    if not arr[left]:
        cur-=1
    left+=1
    right+=1
    if not arr[right]:
        cur+=1
    res=min(res,cur)
print(res)