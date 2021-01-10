# 2847번
import sys
input=sys.stdin.readline

res=0
arr=[]
n=int(input())
for i in range(n):
    arr.append(int(input()))
for i in range(n-1,0,-1):
    if arr[i]<=arr[i-1]:
        res+=arr[i-1]-(arr[i]-1)
        arr[i-1]=arr[i]-1
print(res)
