# 14912번
import sys
input=sys.stdin.readline

n,d=map(int,input().split())
d=str(d)
res=0
for i in range(1,n+1):
    k=str(i)
    if d in k:
        res+=k.count(d)
print(res)