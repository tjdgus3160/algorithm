# 2503번
from itertools import permutations
import sys
input=sys.stdin.readline

def func(ans,x):
    s,b=0,0
    for idx,v in enumerate(x):
        if ans[idx]==v:
            s+=1
        elif v in ans:
            b+=1
    return s,b

arr=[]
for _ in range(int(input())):
    arr.append([*map(int,input().split())])
res=0
for i in permutations(range(1,10),3):
    ans="".join(map(str,i))
    flag=True
    for sub in arr:
        s,b=func(ans,str(sub[0]))
        if s != sub[1] or b != sub[2]:
            flag=False
            break
    if flag:
        res+=1
print(res)