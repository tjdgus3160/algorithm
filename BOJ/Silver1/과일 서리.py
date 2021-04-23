# 17213번
from math import factorial
import sys
input=sys.stdin.readline

def func(a,b): #aCb 계산
    return factorial(a)//(factorial(b)*factorial(a-b))

n=int(input())
m=int(input())
print(func(n-1+m-n,m-n))
