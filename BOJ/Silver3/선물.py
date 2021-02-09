# 1166번
import sys
input=sys.stdin.readline

n,*arr=map(int,input().split())
start=0
end=min(arr)
for _ in range(60):
    mid=(start+end)/2
    k=(arr[0]//mid)*(arr[1]//mid)*(arr[2]//mid)
    if n<=k:
        start=mid
    else:
        end=mid
print(end)