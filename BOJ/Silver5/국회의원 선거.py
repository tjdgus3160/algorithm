#1417번

import sys
input=sys.stdin.readline

n=int(input())
k=int(input())
arr=[]
for i in range(n-1):
    a=int(input())
    if a>=k:
        arr.append(a)
arr.sort()
res=0
while arr and k<=arr[-1]:
    arr[-1]-=1
    k+=1
    res+=1
    arr.sort()
print(res)
