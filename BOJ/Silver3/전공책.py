# 16508번
from itertools import combinations
from collections import Counter
import sys
input=sys.stdin.readline

def check(s,sub):
    tmp=Counter(s)
    for _,c in sub:
        tmp-=c
    if not tmp:
        return True
    return False

s=input().rstrip()
arr=[]
res=0
for _ in range(int(input())):
    c,w=input().rstrip().split()
    tmp=''
    for i in w:
        if i in s:
            tmp+=i
    arr.append((int(c),Counter(tmp)))
arr.sort(key=lambda x:x[0])
res=float('inf')
for i in range(1,len(arr)+1):
    for sub in combinations(arr,i):
        if check(s,sub):
            res=min(res,sum([c for c,_ in sub]))
print(-1 if res==float('inf') else res)