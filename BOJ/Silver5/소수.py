# 1312번
import sys
input=sys.stdin.readline

a,b,n=map(int,input().split())
print(a*pow(10,n)//b%10)
