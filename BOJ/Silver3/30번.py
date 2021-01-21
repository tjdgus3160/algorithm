# 13116번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    a,b=map(int,input().split())
    while a!=b:
        if a<b:
            b//=2
        else:
            a//=2
    print(a*10)

