# 2210번
import sys
input=sys.stdin.readline

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def dfs(x,y,k):
    global res,tmp
    if k==6:
        s=''.join(list(map(str,tmp)))
        if s not in dic:
            dic[s]=1
            res+=1
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<5 and 0<=ny<5:
            tmp.append(arr[ny][nx])
            dfs(nx,ny,k+1)
            tmp.pop()

arr=[]
for _ in range(5):
    arr.append([*map(int,input().split())])
dic={}
res=0
for y in range(5):
    for x in range(5):
        tmp=[arr[y][x]]
        dfs(x,y,1)
print(res)