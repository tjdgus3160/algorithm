# 16171번
import sys
input=sys.stdin.readline

s=''.join([i for i in input().rstrip() if i.isalpha()])
a=input().rstrip()
print(1 if a in s else 0)
