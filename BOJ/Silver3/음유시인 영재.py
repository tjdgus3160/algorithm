# 19948번
from string import ascii_lowercase,ascii_uppercase
import sys
input=sys.stdin.readline

s=input().rstrip()
space=int(input())
arr=[*map(int,input().split())]
prev=None
res=''
for i in s:
    if i==' ':
        if prev==i:
            continue
        space-=1
        if space<0:
            print(-1)
            exit()
    else:
        if prev==i:
            continue
        if prev==' ' or prev==None:
            res+=i.upper()
        if i.islower():
            k=ascii_lowercase.index(i)
        else:
            k=ascii_uppercase.index(i)
        arr[k]-=1
        if arr[k]<0:
            print(-1)
            exit()
    prev=i
for i in res:
    if prev == i:
        continue
    k = ascii_uppercase.index(i)
    arr[k] -= 1
    if arr[k] < 0:
        print(-1)
        exit()
    prev = i
print(res)
