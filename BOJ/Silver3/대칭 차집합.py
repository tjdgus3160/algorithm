# 1269번
import sys
input=sys.stdin.readline

input()
a=set(map(int,input().split()))
b=set(map(int,input().split()))
t=a.union(b)
k=a.intersection(b)
print(len(t.difference(k)))