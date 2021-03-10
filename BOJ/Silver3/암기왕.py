# 2776번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    arr1=[*map(int,input().split())]
    dic=set(arr1)
    m=int(input())
    arr2=[*map(int,input().split())]
    for i in arr2:
        if i in dic:
            print(1)
        else:
            print(0)