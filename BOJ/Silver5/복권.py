# 1359번
from itertools import combinations
import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())

a=list(combinations([*range(1,n+1)],m))
b=list(combinations([*range(1,n+1)],m))
res=0
for i in a:
    for j in b:
        tmp=[1 for q in range(m) if i[q] in j]
        if len(tmp)>=k:
            res+=1
print(res/pow(len(a),2))