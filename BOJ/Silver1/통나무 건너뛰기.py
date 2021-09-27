# 11497번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    arr=sorted([*map(int,input().split())])
    a=[]
    b=[]
    for i in range(n):
        if i%2==0:
            a.append(arr[i])
        else:
            b.append(arr[i])
    c=a+b[::-1]
    res=-float('inf')
    for i in range(1,n):
        res=max(res,abs(c[i]-c[i-1]))
    print(res)
