# 2078번
import sys
input=sys.stdin.readline

l,r=0,0
a,b=map(int,input().split())
while a>1 and b>1:
    if a<b:
        b-=a
        r+=1
    else:
        a-=b
        l+=1
l+=a-1
r+=b-1
print(l,r)