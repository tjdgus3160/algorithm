import sys
input=sys.stdin.readline

a=[*map(int,input().split())]
a.sort()
print(a[len(a)//2])
