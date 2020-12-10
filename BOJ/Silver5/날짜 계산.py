# 1476번
import sys
input=sys.stdin.readline

e,s,m=map(int,input().split())
a=0
b=0
c=0
res=0
while e!=a or s!=b or m!=c:
    res+=1
    a+=1
    if a>15:
        a=1
    b+=1
    if b>28:
        b=1
    c+=1
    if c>19:
        c=1
print(res)