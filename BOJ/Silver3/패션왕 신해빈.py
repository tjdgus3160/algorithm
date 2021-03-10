# 9375번
from collections import defaultdict
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    dic=defaultdict(list)
    for _ in range(int(input())):
        v,idx=input().split()
        dic[idx].append(v)
    if len(dic.keys())==1:
        print(len(*dic.values()))
    else:
        res=1
        for sub in dic.values():
            res*=len(sub)+1
        print(res-1)