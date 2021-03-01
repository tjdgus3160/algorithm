# 17504번
import sys
input=sys.stdin.readline

n=int(input())
arr=[*map(int,input().split())]

up=1
down=arr.pop()
while arr:
    k=arr.pop()
    up=k*down+up
    up,down = down,up
print(down-up,down)