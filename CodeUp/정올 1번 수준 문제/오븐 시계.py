import sys
input=sys.stdin.readline

a,b=map(int,input().split())
n=int(input())
b+=n
if b>=60:
    a+=b//60
    b%=60
if a>=24:
    a-=24
print(a,b)
