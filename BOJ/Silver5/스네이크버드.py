# 16435번
import sys
input=sys.stdin.readline

n,l=map(int,input().split())
arr=[*map(int,input().split())]
arr.sort()
for i in range(len(arr)):
    if arr[i]<=l:
        l+=1
    else:
        break
print(l)