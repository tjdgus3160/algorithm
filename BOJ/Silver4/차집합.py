# 1822번
import sys
input=sys.stdin.readline

input()
a=set([*map(int,input().split())])
b=set([*map(int,input().split())])
res=a.difference(b)
print(len(res))
print(*sorted(list(res)))