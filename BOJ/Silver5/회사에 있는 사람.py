# 7785번
import sys
input=sys.stdin.readline

p={}
for _ in range(int(input())):
    s,a=input().split()
    if a=='enter':
        p[s]=1
    else:
        p[s]=0
res=sorted(p.keys(),reverse=True)
for i in res:
    if p[i]:
        print(i)