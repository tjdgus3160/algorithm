# 1940번
import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
arr=[*map(int,input().split())]
res=0
for i in arr:
    if m-i in arr:
        res+=1
print(res//2)