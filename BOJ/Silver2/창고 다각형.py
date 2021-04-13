# 2304번
import sys
input=sys.stdin.readline

n=int(input())
arr=[]
maxh=0
maxl=0
for _ in range(n):
    l,h=map(int,input().split())
    if h>maxh:
        maxl=l
        maxh=h
    arr.append((l,h))
arr.sort()
left=0
curh=0
curl=0
for l,h in arr:
    if l==maxl:
        left+=(l-curl)*curh
        break
    if not curh:
        curl=l
        curh=h
        continue
    if curh<h:
        left+=(l-curl)*curh
        curl=l
        curh=h
right=0
curh=0
curl=0
arr.reverse()
for l,h in arr:
    if l==maxl:
        right+=(curl-l)*curh
        break
    if not curh:
        curl=l
        curh=h
        continue
    if curh<h:
        right+=(curl-l)*curh
        curl=l
        curh=h
print(left+right+maxh)
