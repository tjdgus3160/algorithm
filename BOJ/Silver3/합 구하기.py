# 11441번
import sys
input=sys.stdin.readline

n=int(input())
arr=[0,*map(int,input().split())]
for i in range(2,n+1):
    arr[i]+=arr[i-1]
for _ in range(int(input())):
    a,b=map(int,input().split())
    print(arr[b]-arr[a-1])