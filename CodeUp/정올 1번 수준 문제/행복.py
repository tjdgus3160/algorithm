import sys
input=sys.stdin.readline

n=int(input())
a=[*map(int,input().split())]
print(max(a)-min(a))
