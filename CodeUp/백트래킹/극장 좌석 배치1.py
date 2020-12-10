from math import factorial
import sys
input=sys.stdin.readline

a,b=map(int,input().split())
print(factorial(a)//factorial(b)//factorial(a-b))
