# 1026번
import sys
input=sys.stdin.readline

n=int(input())
a=[*map(int,input().split())]
b=[*map(int,input().split())]
a.sort()
b.sort()
b.reverse()
res=0
for i in range(len(a)):
    res+=a[i]*b[i]
print(res)