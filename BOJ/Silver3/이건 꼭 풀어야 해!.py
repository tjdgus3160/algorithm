# 17390번
import sys
input=sys.stdin.readline

n,q=map(int,input().split())
arr=[0,*map(int,input().split())]
arr.sort()
for i in range(2,n+1):
    arr[i]+=arr[i-1]
for _ in range(q):
    l,r=map(int,input().split())
    print(arr[r]-arr[l-1])