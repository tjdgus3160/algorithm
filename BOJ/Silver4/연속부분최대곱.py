# 2670번
import sys
input=sys.stdin.readline

n=int(input())
arr=[0]*n
for i in range(n):
    k=float(input())
    if i==0:
        arr[0]=k
        continue
    arr[i]=max(k,k*arr[i-1])
print("%.3f"%(max(arr)))