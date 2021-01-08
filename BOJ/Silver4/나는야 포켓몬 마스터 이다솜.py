# 1620번
import sys
input=sys.stdin.readline

num={}
name={}
n,m=map(int,input().split())
for i in range(1,n+1):
    s=input().rstrip("\n")
    name[s]=i
    num[i]=s
for _ in range(m):
    k=input().rstrip("\n")
    if k[0].isdigit():
        print(num[int(k)])
    else:
        print(name[k])