from itertools import combinations
import sys
input=sys.stdin.readline

n,s=map(int,input().split())
arr=[*map(int,input().split())]

if n==1 and s in arr:
    print(1)
else:
    res=0
    for i in range(1,n):
        for sub in combinations(arr,i):
            if sum(sub)==s:
                res+=1
    print(res)
