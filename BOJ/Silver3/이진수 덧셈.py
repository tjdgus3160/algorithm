# 2729번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    a,b=input().rstrip('\n').split()
    res=int(a,2)+int(b,2)
    print(bin(res)[2:])