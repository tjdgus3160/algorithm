# 2599번
import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(3):
    arr+=[*map(int,input().split())]
flag=True

for i in range(arr[0]+1):
    a=i
    b=arr[0]-a
    d=arr[5]-b
    c=arr[2]-d
    e=arr[1]-c
    f=arr[4]-e
    if a>=0 and b>=0 and c>=0 and d>=0 and e>=0 and f>=0:
        print(1)
        print(a,b)
        print(c,d)
        print(e,f)
        flag=False
        break
if flag:
    print(0)