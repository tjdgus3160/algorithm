from itertools import product
import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
move=[*map(int,input().split())]

res=0
for sub in product([*range(k)],repeat=n):
    arr=[1]*k
    for idx,v in zip(sub,move):
        arr[idx]+=v
    res=max(res,len([True for i in arr if i>=m]))
print(res)