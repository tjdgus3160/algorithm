# 13417번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    arr=input().split()
    res=arr.pop(0)
    while arr:
        if res[0]>=arr[0]:
            res=arr.pop(0)+res
        else:
            res=res+arr.pop(0)
    print(res)