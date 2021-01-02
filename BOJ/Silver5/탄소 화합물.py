# 1907번
from itertools import product
import copy
import sys
input=sys.stdin.readline

def func(s):
    tmp = ""
    for idx, v in enumerate(s):
        if v.isdigit():
            tmp += s[idx - 1] * (int(v) - 1)
        else:
            tmp += v
    d={}
    for s in tmp:
        d.setdefault(s, 0)
        d[s] += 1
    return d

s=input().rstrip('\n')
s1=func(s[:s.find("+")])
s2=func(s[s.find("+")+1:s.find("=")])
s3=func(s[s.find("=")+1:])
for a,b,c in product(range(1,11),repeat=3):
    d1=copy.deepcopy(s1)
    d2=copy.deepcopy(s2)
    d3=copy.deepcopy(s3)
    for i in d1.keys():
        d1[i]*=a
    for i in d2.keys():
        d2[i]*=b
    flag=True
    for i in d3.keys():
        k=0
        if i in d1:
            k+=d1[i]
        if i in d2:
            k+=d2[i]
        if d3[i]*c!=k:
            flag=False
            break
    if flag:
        print(a,b,c)
        break