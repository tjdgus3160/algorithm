# 16943번
from itertools import permutations
import sys
input=sys.stdin.readline

a,b=map(int,input().split())
res=-1
for sub in permutations(str(a),len(str(a))):
    if sub[0]=='0': continue
    k=int(''.join(sub))
    if k<b:
        res=max(res,k)
print(res)