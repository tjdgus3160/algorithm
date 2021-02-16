# 1654번
import sys
input=sys.stdin.readline

k,n=map(int,input().split())
arr=[]
for _ in range(k):
    arr.append(int(input()))
res=0
start=0
end=max(arr)
if end==1:
    print(1)
elif n==1:
    print(end)
else:
    while start<end:
        mid=(start+end+1)//2
        cnt=sum([i//mid for i in arr])
        if cnt>=n:
            start = mid
        else:
            end = mid-1
    print(start)