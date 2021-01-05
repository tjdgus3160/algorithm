# 11650번
import sys
input=sys.stdin.readline

arr=[]
for _ in range(int(input())):
    arr.append([*map(int,input().split())])
for i in sorted(arr,key=lambda x:(x[0],x[1])):
    print(*i)