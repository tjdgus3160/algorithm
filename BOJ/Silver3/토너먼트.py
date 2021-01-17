# 1057번
from collections import deque
import sys
input=sys.stdin.readline

n,a,b=map(int,input().split())
if a>b:
    a,b=b,a
arr=deque([*range(1,n+1)])
total=n
res=1
flag=False
while True:
    for i in range(total//2):
        if arr[2*i]==a and arr[2*i+1]==b:
            flag=True
            break
        arr[i]=arr[2*i+1] if a==arr[2*i+1] or b==arr[2*i+1] else arr[2*i]
    if total%2==1:
        arr[total//2]=arr[2*(total//2)]
    if flag:
        break
    res+=1
    if total%2==0:
        total//=2
    else:
        total//=2
        total+=1
print(res)