# 2485번
from math import gcd
import sys
input=sys.stdin.readline

arr=[]
n=int(input())
for _ in range(n):
    arr.append(int(input()))
arr.sort()
l=arr[1]-arr[0]
for i in range(1,n-1):
    l=gcd(arr[i+1]-arr[i],l)

print((arr[-1]-arr[0])//l-n+1)