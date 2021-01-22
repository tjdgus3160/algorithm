# 11170번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n,m=map(int,input().split())
    res=0
    for i in range(n,m+1):
        s=list(str(i))
        res+=s.count('0')
    print(res)