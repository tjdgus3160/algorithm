# 17219번
import sys
input=sys.stdin.readline

dic={}
m,n=map(int,input().split())
for _ in range(m):
    s,p=input().split()
    dic[s]=p
for _ in range(n):
    s=input().rstrip('\n')
    print(dic[s])