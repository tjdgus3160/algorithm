# 14889번
from itertools import combinations
import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    arr.append([*map(int,input().split())])
res=float('inf')
for start in combinations([*range(n)],n//2):
    a,b=0,0
    for i in range(n//2):
        for j in range(i+1,n//2):
            a+=(arr[start[i]][start[j]]+arr[start[j]][start[i]])
    link=[i for i in range(n) if i not in start]
    for i in range(n//2):
        for j in range(i+1,n//2):
            b+=(arr[link[i]][link[j]]+arr[link[j]][link[i]])
    res=min(res,abs(a-b))
print(res)