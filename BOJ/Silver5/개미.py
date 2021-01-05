# 10158번
import sys
input=sys.stdin.readline

w,h=map(int,input().split())
p,q=map(int,input().split())
t=int(input())
if t<=(w-p):
    x=p+t
else:
    tmp=t-(w-p)
    if (tmp//w)%2==0:
        x=w-(tmp%w)
    else:
        x=tmp%w
if t<=(h-q):
    y=q+t
else:
    tmp=t-(h-q)
    if (tmp//h)%2==0:
        y=h-(tmp%h)
    else:
        y = tmp % h
print(x,y)