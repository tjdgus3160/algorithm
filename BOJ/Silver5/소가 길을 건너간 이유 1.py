# 14467번
import sys
input=sys.stdin.readline

n=int(input())
cow=[-1]*11
res=0
for _ in range(n):
    a,b=map(int,input().split())
    if cow[a]==-1:
        cow[a]=b
    else:
        if cow[a]!=b:
            cow[a] = b
            res+=1
print(res)