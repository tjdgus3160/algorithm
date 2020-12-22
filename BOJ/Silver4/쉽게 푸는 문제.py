# 1292번
import sys
input=sys.stdin.readline

a,b=map(int,input().split())
arr=[0]
for i in range(1,46):
    arr+=[i]*i
print(sum(arr[a:b+1]))