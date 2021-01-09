# 1244번
import sys
input=sys.stdin.readline

n=int(input())
arr=[*map(int,input().split())]
for _ in range(int(input())):
    s,k=map(int,input().split())
    if s==1:
        for i in range(k-1,n,k):
            arr[i]=0 if arr[i]==1 else 1
    else:
        k-=1
        arr[k]=0 if arr[k]==1 else 1
        for i in range(1,min(n-k+1,k+1)):
            if 0<=k-i<n and 0<=k+i<n and arr[k-i]==arr[k+i]:
                if arr[k-i]:
                    arr[k-i],arr[k+i]=0,0
                else:
                    arr[k-i],arr[k+i]=1,1
            else:
                break
for i in range(n//20+1):
    print(*arr[i*20:i*20+20])