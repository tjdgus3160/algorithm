import sys
input=sys.stdin.readline

n,k=map(int,input().split())
a=[*map(int,input().split())]

res=sum(a[0:k])
tmp=res
for i in range(n-k):
    tmp=tmp-a[i]+a[i+k]
    if res<tmp:
        res=tmp
print(res)
