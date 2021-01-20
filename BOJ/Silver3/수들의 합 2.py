# 2003번
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[*map(int,input().split())]
start=0
end=0
res=0
k=arr[0]
while True:
    if k<m:
        end+=1
        k+=arr[end]
    elif k>m:
        k-=arr[start]
        start+=1
    else:
        res+=1
        if end==n-1:
            break
        end+=1
        k+=arr[end]
    if (end==n-1 and k<m):
        break
print(res)
