# 19939번
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
if n<k*(k+1)//2:
    print(-1)
else:
    n-=(k*(k+1)//2)
    if n%k:
        print(k)
    else:
        print(k-1)