# 1246번
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[]
for _ in range(m):
    arr.append(int(input()))
arr.sort(reverse=True)
cost=0
total=0
for i,v in enumerate(arr):
    if (i+1)>n:
        break
    if total<v*(i+1):
        total=v*(i+1)
        cost=v
print(cost,total)