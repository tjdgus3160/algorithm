from math import factorial
import sys
input=sys.stdin.readline

def find(n,r):
    return factorial(n)//factorial(r)//factorial(n-r)
n,r=map(int,input().split())
print(find(n,r))

