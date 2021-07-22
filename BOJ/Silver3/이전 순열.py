# 10973번
import sys
input=sys.stdin.readline

n=int(input())
arr=[*map(int,input().split())]

if sorted(arr)==arr:
    print(-1)
    exit()

k=None
p=None
for i in range(len(arr)-2,-1,-1):
    if arr[i]>arr[i+1]:
        k=i
        for j in range(len(arr)-1,k,-1):
            if arr[j]<arr[k]:
                p=j
                break
        break
arr[k],arr[j]=arr[j],arr[k]
res=arr[:k+1]+sorted(arr[k+1:],reverse=True)
print(*res)