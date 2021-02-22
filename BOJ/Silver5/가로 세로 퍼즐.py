# 2784번
from itertools import permutations
import copy
import sys
input=sys.stdin.readline

arr=[]
for _ in range(6):
    arr.append(input().rstrip('\n'))

res=[]
flag=True
for sub in permutations(arr,3):
    tmp=copy.deepcopy(arr)
    tmp.remove(sub[0])
    tmp.remove(sub[1])
    tmp.remove(sub[2])
    for s in zip(*sub):
        k=''.join(s)
        if k not in tmp:
            break
        tmp.remove(k)
    else:
        for i in range(3):
            print(sub[i])
        flag=False
        break
if flag:
    print(0)

