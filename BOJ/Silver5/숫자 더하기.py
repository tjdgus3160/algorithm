# 9440번
import sys
input=sys.stdin.readline

while True:
    line=input().split()
    if len(line)==1:
        break
    n,*arr=line
    arr.sort()
    cnt=arr.count('0')
    a=[]
    b=[]
    for i in range(cnt,int(n)):
        if i%2==0:
            b.append(arr[i])
        else:
            a.append(arr[i])
    m,r=divmod(cnt,2)
    a=[a[0]]+['0']*m+a[1:]
    b=[b[0]]+['0']*m+b[1:]
    if r:
        if len(a)<len(b):
            a=[a[0]]+['0']+a[1:]
        elif len(a)>len(b):
            b=[b[0]]+['0']+b[1:]
        elif a[0]<b[0]:
            a = [a[0]] + ['0'] + a[1:]
        else:
            b = [b[0]] + ['0'] + b[1:]
    print(int(''.join(a))+int(''.join(b)))