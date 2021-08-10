from itertools import combinations
import sys
input=sys.stdin.readline

n=int(input())
arr=[*map(int,input().split())]
tmp=[]
for sub in combinations(arr,n):
    tmp.append(sum(sub))
res=float('inf')
for i in range(len(tmp)//2):
    res=min(res,abs(tmp[i]-tmp[-1-i]))
print(res)