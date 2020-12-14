# 1629번
import sys
input=sys.stdin.readline

def fund(a,b,c):
    if a>10**8:
        a%=c
    if b==1:
        return a
    if b%2==0:
        return fund(a**2,b//2,c)
    else:
        return a*fund(a**2,b//2,c)

a,b,c=map(int,input().split())
print(fund(a,b,c)%c)

# print(pow(*map(int,input().split()))) 더 간단한 방법