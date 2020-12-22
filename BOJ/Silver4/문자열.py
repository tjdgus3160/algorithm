# 1120번
import sys
input=sys.stdin.readline

a,b=input().split()
res=999
for i in range(len(b)-len(a)+1):
    tmp=len([1 for x,y in zip(a,b[i:i+len(a)]) if x!=y])
    res=min(res,tmp)
print(res)