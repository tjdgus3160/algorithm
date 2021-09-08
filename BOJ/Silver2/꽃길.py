# 14620번
from itertools import combinations
import sys
input=sys.stdin.readline

def vaild(sub):
    for x,y in sub:
        if x==0 or x==n-1 or y==0 or y==n-1:
            return False
    for i in range(2):
        for j in range(i+1,3):
            if abs(sub[i][0]-sub[j][0])+abs(sub[i][1]-sub[j][1])<3:
                return False
    return True

def check(sub):
    res=0
    for x,y in sub:
        res+=arr[x][y]
        for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            res+=arr[nx][ny]
    return res

n=int(input())
arr=[[*map(int,input().split())]for _ in range(n)]
loc=[(i,j) for i in range(n) for j in range(n)]
res=float('inf')
for sub in combinations(loc,3):
    if vaild(sub):
        res=min(res,check(sub))
print(res)