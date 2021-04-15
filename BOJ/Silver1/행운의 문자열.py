# 1342번
from math import factorial
from collections import Counter
from itertools import permutations
import sys
input=sys.stdin.readline

s=input().rstrip('\n')
tmp=[]
c=Counter(s)
res=0
for sub in permutations(s,len(s)):
    for i in range(1,len(sub)):
        if sub[i]==sub[i-1]:
            break
    else:
        res+=1
for k in c.values():
    res//=factorial(k)
print(res)