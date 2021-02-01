# 12782번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    a,b=input().rstrip('\n').split()
    diff=[(a,b) for a,b in zip(a,b) if a!=b]
    print(max(diff.count(('0','1')),diff.count(('1','0'))))