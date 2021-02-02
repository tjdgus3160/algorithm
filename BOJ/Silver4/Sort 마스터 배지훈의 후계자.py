# 20551번
import bisect
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[]
for _ in range(n):
    bisect.insort(arr,int(input()))
for _ in range(m):
    k=int(input())
    loc=bisect.bisect_left(arr,k)
    print(loc if loc<len(arr) and arr[loc]==k else -1)