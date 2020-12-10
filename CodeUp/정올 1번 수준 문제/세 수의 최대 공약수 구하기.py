import sys
input=sys.stdin.readline

def gcd(a,b):
    result=0
    while(b!=0):
        result=b
        a,b=b,a%b
    return result

a,b,c=map(int,input().split())
print(gcd(gcd(a,b),c))
