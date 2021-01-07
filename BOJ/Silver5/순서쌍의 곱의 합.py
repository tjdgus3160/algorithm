# 13900번
import sys
input=sys.stdin.readline

n=int(input())
res=0
total=0
for v in [*map(int,input().split())]:
    if total==0:
        total+=v
    else:
        res+=total*v
        total+=v
print(res)