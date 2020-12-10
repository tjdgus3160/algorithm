# 1010번
from math import factorial
import sys
input=sys.stdin.readline

res=[]
for _ in range(int(input())):
    a,b=map(int,input().split())
    res.append(factorial(b)//factorial(a)//factorial(b-a))
for i in res:
    print(i)