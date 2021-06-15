# 14241번
import sys
input=sys.stdin.readline

input()
arr=[*map(int,input().split())]
arr.sort()
res=0
while len(arr)>1:
    k=arr.pop()
    res+=k*arr[-1]
    arr[-1]+=k
print(res)