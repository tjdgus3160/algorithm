# 7795번
import bisect
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n,m=map(int,input().split())
    a=[*map(int,input().split())]
    b=[*map(int,input().split())]
    b.sort()
    print(sum([bisect.bisect_left(b,i) for i in a]))