# 11728번
import sys
input=sys.stdin.readline

arr=[]
for _ in range(int(input())):
    arr.append(int(input()))
for i in sorted(arr,reverse=True):
    print(i)