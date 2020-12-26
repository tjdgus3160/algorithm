# 1205번
import sys
input=sys.stdin.readline

n,k,p=map(int,input().split())
if n==0:
    print(1)
else:
    arr = [*map(int, input().split())]
    arr.append(k)
    arr.sort(reverse=True)
    res=arr.index(k)
    if n==p:
        print(res+1 if res+arr.count(k)<=p else -1)
    else:
        print(res+1 if res <= p else -1)
