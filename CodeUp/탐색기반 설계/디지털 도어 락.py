from math import gcd
import sys
input=sys.stdin.readline

a,b,c=map(int,input().split())
print(gcd(gcd(a,b),c))

