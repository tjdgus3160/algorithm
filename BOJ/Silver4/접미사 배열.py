# 11656번
import sys
input=sys.stdin.readline

s=input().rstrip('\n')
arr=[]
for i in range(len(s)):
    arr.append(s[i:])
for i in sorted(arr):
    print(i)