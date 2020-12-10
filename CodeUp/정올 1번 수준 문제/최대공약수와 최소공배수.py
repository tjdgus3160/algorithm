from math import gcd
import sys
input=sys.stdin.readline

def lcm(a,b):
    return a*b//gcd(a,b)

a,b=map(int,input().split())
print(gcd(a,b))
print(lcm(a,b))
