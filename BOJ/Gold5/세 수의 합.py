# 2295번
import sys
input=sys.stdin.readline

n=int(input())
arr=sorted([int(input()) for _ in range(n)])
two=set()
for i in range(n):
    for j in range(i,n):
        two.add(arr[i]+arr[j])

for i in range(n-1,0,-1):
    for j in range(i):
        if arr[i]-arr[j] in two:
            print(arr[i])
            exit()