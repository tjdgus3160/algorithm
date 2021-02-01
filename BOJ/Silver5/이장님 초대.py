# 9237번
import sys
input=sys.stdin.readline

n=int(input())
arr=[*map(int,input().split())]
arr.sort(reverse=True)
res=0
for idx,v in enumerate(arr):
    res=max(res,idx+v)
print(res+2)