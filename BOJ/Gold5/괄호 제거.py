# 2800번
from itertools import combinations
import sys
input=sys.stdin.readline

s=list(input().rstrip())
stack=[]
pair=[]
for idx,v in enumerate(s):
    if v=='(':
        stack.append((idx))
    elif v==')':
        pair.append([stack.pop(),idx])
res=set()
for i in range(1,len(pair)+1):
    for sub in combinations(pair,i):
        k=s[:]
        for i,j in sub:
            k[i],k[j]='',''
        res.add(''.join(k))
for i in sorted(res):
    print(i)