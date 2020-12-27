# 1564번
import sys
input=sys.stdin.readline

n=int(input())
num=1
for i in range(2,n+1):
    num*=i
    while num%10==0:
        num//=10
    num%=1000000000000
num%=100000
print(str(num).rjust(5,'0'))