# 11653번
import sys
input=sys.stdin.readline

n=int(input())
arr=[]
while n>1:
    for i in range(2,n+1):
        if n%i==0:
            arr.append(i)
            n//=i
            break
for i in sorted(arr):
    print(i)