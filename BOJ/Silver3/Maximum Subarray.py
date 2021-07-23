# 10211번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    arr=[*map(int,input().split())]
    if max(arr)<0:
        print(max(arr))
        continue
    k=0
    res=0
    for i in arr:
        k+=i
        if k<0:
            k=0
        else:
            res=max(res,k)
    print(res)