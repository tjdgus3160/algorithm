# 9322번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    arr1=input().split()
    arr2=input().split()
    tmp=input().split()
    res=[]
    for i in arr1:
        k=arr2.index(i)
        res.append(tmp[k])
    print(*res)