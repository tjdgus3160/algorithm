# 18111번
from collections import defaultdict
import sys
input=sys.stdin.readline

n,m,b=map(int,input().split())
dic=defaultdict(int)
big,small=0,256
for _ in range(n):
    for i in map(int,input().split()):
        dic[i]+=1
        big=max(big,i)
        small=min(small,i)

res=float('inf')
height=None
for h in range(big,small-1,-1):
    acc=b
    time=0
    fail=False
    for key,value in sorted(dic.items(),reverse=True):
        if key>h:
            acc+=(key-h)*value
            time+=(key-h)*value*2
        elif key<h:
            acc-=(h-key)*value
            if acc<0:
                fail=True
                break
            time+=(h-key)*value
    if not fail:
        if res>time:
            res=time
            height=h
        else:
            break
print(res,height)