# 2548번
import sys
input=sys.stdin.readline

n=int(input())
arr=[*map(int,input().split())]
arr.sort()
print(arr[(n-1)//2])