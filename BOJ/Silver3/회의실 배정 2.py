# 19621번
import sys
input=sys.stdin.readline

def dfs(t,cnt):
    global res
    if t>=arr[-1][0]:
        res=max(res,cnt)
        return
    for i in range(len(arr)):
        if t<arr[i][0]:
            dfs(arr[i][1],cnt+arr[i][2])

n=int(input())
arr=[]
res=0
for _ in range(n):
    arr.append([*map(int,input().split())])
arr.sort(key=lambda x:x[1])
dfs(0,0)
print(res)