# 2841번
import sys
input=sys.stdin.readline

n,p=map(int,input().split())
res=0
arr=[[] for _ in range(n+1)]
for _ in range(n):
    a,b=map(int,input().split())
    while arr[a] and arr[a][-1]>b:
        arr[a].pop()
        res+=1
    if arr[a] and arr[a][-1]==b:
        continue
    arr[a].append(b)
    res += 1
print(res)