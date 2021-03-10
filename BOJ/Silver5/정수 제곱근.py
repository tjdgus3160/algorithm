# 2417번
import sys
input=sys.stdin.readline

n=int(input())
start=1
end=n
while start<end:
    mid=(start+end)//2
    k=pow(mid,2)
    if k<n:
        start=mid+1
    else:
        end=mid
print(end)