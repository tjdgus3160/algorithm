# 1092번
from bisect import bisect
import sys
input=sys.stdin.readline

n=int(input())
arr=sorted([*map(int,input().split())],reverse=True)
m=int(input())
box=sorted([*map(int,input().split())])
if max(box)>max(arr):
    print(-1)
    exit()
res=0
while box:
    for i in arr:
        k=bisect(box,i)
        if not k and box[k]>i:
            continue
        del box[k-1]
        if not box:
            break
    res+=1
print(res)
