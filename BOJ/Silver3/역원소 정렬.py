# 5648번
import sys
input=sys.stdin.readline

arr=[]
n,*tmp=map(int,input().split())
for i in tmp:
    k=list(str(i))
    k.reverse()
    arr.append(int(''.join(k)))
while len(arr)<n:
    tmp=map(int, input().split())
    for i in tmp:
        k = list(str(i))
        k.reverse()
        arr.append(int(''.join(k)))
for i in sorted(arr):
    print(i)

