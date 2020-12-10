from math import factorial
import sys
input=sys.stdin.readline

a,b=map(int,input().split())
if a+1<2*b:
    print(0)
else:
    print(factorial(a-b+1)//factorial(b)//factorial(a-2*b+1))
