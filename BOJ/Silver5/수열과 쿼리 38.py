# 18917번
import sys
input=sys.stdin.readline

a,b=0,0
for _ in range(int(input())):
    i,*x=map(int,input().split())
    if i==1:
        a+=x[0]
        b^=x[0]
    elif i==2:
        a-=x[0]
        b^=x[0]
    elif i==3:
        print(a)
    else:
        print(b)