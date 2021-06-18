# 10971번
import sys
input=sys.stdin.readline

res=float('inf')
def func(k,cur,total):
    global res
    if k==n and cur==0:
        res=min(res,total)
        return
    for i in range(n):
        if i==cur or (k<n-1 and i==0):
            continue
        if not visited[i] and arr[cur][i]:
            visited[i]=True
            func(k+1,i,total+arr[cur][i])
            visited[i]=False

n=int(input())
arr=[[*map(int,input().split())] for _ in range(n)]

visited = [False] * n
func(0,0,0)
print(res)