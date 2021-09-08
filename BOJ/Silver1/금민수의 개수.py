# 1527번
from itertools import product
import sys
input=sys.stdin.readline

a,b=map(int,input().split())
res=0
for i in range(len(str(a)),len(str(b))+1):
    for sub in product([4,7],repeat=i):
        if a<=int(''.join([str(v) for v in sub]))<=b:
            res+=1
print(res)
