# 16283번
import sys
input=sys.stdin.readline

a,b,n,w=map(int,input().split())
if a==b:
    if w//a==2 and n==2:
        print(1,1)
    else:
        print(-1)
elif (a*n-w)%(a-b)!=0:
    print(-1)
else:
    y=(a*n-w)//(a-b)
    x=n-y
    if x!=0 and y!=0:
        print(x,y)
    else:
        print(-1)