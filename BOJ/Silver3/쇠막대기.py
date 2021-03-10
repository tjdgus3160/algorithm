# 10799번
import sys
input=sys.stdin.readline

s=input().rstrip('\n')

res=0
k=0
prv=''
for i in s:
    if prv=='':
        prv=i
        k+=1
        continue
    if i==')':
        k-=1
        if prv=='(':
            res+=k
        else:
            res+=1
    else:
        k+=1
    prv=i
print(res)