# 13251번
import sys
input=sys.stdin.readline

m=int(input())
arr=[*map(int,input().split())]
n=sum(arr)
k=int(input())
total=1
for i in range(k):
    total*=(n-i)
res=0
for v in arr:
    if v>=k:
        tmp=1
        for i in range(k):
            tmp*=(v-i)
        res+=tmp
print(res/total)