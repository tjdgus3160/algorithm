# 14584번
import sys
input=sys.stdin.readline

s=input().rstrip()
arr=[input().rstrip() for _ in range(int(input()))]
for _ in range(26):
    for i in arr:
        if i in s:
            print(s)
            break
    tmp=''
    for i in s:
        k=ord(i)+1
        if k>122:
            k-=26
        tmp+=chr(k)
    s=tmp