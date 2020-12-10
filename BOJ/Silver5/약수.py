# 1037번
import sys
input=sys.stdin.readline

n=int(input())
l=[*map(int,input().split())]
l.sort()
if n==1:
    print(l[0]**2)
else:
    print(l[0]*l[-1])