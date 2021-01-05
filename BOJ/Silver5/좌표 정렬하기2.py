# 11650번
import sys
input=sys.stdin.readline

arr=[]
for _ in range(int(input())):
    arr.append([*map(int,input().split())])
for i in sorted(arr,key=lambda x:(x[1],x[0])):
    print(*i)