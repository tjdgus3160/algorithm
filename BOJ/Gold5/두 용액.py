# 2470번
import sys
input=sys.stdin.readline

n=int(input())
arr=sorted([*map(int,input().split())])
start=0
end=n-1
res=[]
k=float('inf')
while start<end:
    v=arr[end]+arr[start]
    if k>abs(v):
        res = [arr[start], arr[end]]
        k=abs(v)
    if abs(arr[start])<abs(arr[end]):
        end-=1
    else:
        start+=1
print(*res)
