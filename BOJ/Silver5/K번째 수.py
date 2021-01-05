# 11004번
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
arr=[*map(int,input().split())]
arr.sort()
print(arr[k-1])