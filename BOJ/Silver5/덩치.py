# 7568번
import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    arr.append([*map(int,input().split())])

res=[0]*n
for i in range(n):
    k=1
    for j in range(n):
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            k+=1
    res[i]=k
print(*res)