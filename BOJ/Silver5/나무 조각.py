# 2947번
import sys
input=sys.stdin.readline

arr=[*map(int,input().split())]
while arr!=sorted(arr):
    for i in range(4):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            print(*arr)