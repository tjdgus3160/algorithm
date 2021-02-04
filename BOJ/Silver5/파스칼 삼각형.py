# 15489번
import sys
input=sys.stdin.readline

arr=[[1]for _ in range(30)]
for i in range(1,30):
    for j in range(1,i):
        arr[i].append(arr[i-1][j-1]+arr[i-1][j])
    arr[i].append(1)
r,c,w=map(int,input().split())
res=0
for i in range(1,w+1):
    res+=sum(arr[r+i-2][c-1:c+i-1])
print(res)