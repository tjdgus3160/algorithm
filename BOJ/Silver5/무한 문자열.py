# 12871번
import sys
input=sys.stdin.readline

s=input().rstrip('\n')
t=input().rstrip('\n')
s*=100
t*=100
print(int(s[:100]==t[:100]))