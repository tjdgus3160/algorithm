# 16173번
import sys
input=sys.stdin.readline

def dfs(x,y):
    global res
    if arr[y][x]==-1:
        res='HaruHaru'
        return
    if not arr[y][x]:
        return 
    if res=='Hing':
        if x+arr[y][x]<len(arr):
            dfs(x+arr[y][x],y)
        if y+arr[y][x]<len(arr):
            dfs(x,y+arr[y][x])

arr=[[*map(int,input().split())] for _ in range(int(input()))]
res='Hing'
dfs(0,0)
print(res)