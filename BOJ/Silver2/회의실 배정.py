# 1931번
import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    s,e=map(int,input().split())
    arr.append((s,e))
arr.sort(key=lambda x:(x[1],x[0]))
res=[arr[0]]
for i in arr[1:]:
    if res[-1][1]<=i[0]:
        res.append(i)
print(len(res))
