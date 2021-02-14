# 1446번
import sys
input=sys.stdin.readline

n,d=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append([*map(int,input().split())])
res=[i for i in range(d+1)]
for i in range(d+1):
    if i:
        res[i]=min(res[i],res[i-1]+1)
    for s,e,w in arr:
        if s==i and e<=d:
            res[e]=min(res[e],res[s]+w)
print(res[d])