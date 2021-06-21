# 1337번
import sys
input=sys.stdin.readline

n=int(input())
arr=[int(input()) for _ in range(n)]
arr.sort()

res=float('inf')
for i in range(n):
    cnt=1
    for j in range(i+1,i+5):
        if j<n and arr[j]<arr[i]+5:
            cnt+=1
    res=min(res,abs(5-cnt))
print(res)