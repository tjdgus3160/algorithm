# 15970번
import sys
input=sys.stdin.readline

arr=[]
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    arr.append([a,b])
arr.sort(key=lambda x:(x[1],x[0]))
res=0
t=-1
for i in range(n):
    if t==-1:
        t=arr[i][1]
        if i + 1 < n and arr[i + 1][1] == t:
            res+=arr[i+1][0]-arr[i][0]
    elif arr[i][1]==t:
        if i+1<n and arr[i+1][1]==t:
            res+=min(arr[i+1][0]-arr[i][0],arr[i][0]-arr[i-1][0])
        else:
            res+=arr[i][0]-arr[i-1][0]
    else:
        t=arr[i][1]
        if i+1<n and arr[i+1][1]==t:
            res+=arr[i+1][0]-arr[i][0]
print(res)