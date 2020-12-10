import copy
import sys
input=sys.stdin.readline

def dfs(x,y,k):
    stack=[[x,y]]
    while stack:
        x,y=stack.pop()
        tmp[y][x]=k
        if x>0 and tmp[y][x-1]!=k:
            stack.append([x-1,y])
        if x<m-1 and tmp[y][x+1]!=k:
            stack.append([x+1,y])
        if y>0 and tmp[y-1][x]!=k:
            stack.append([x,y-1])
        if y<n-1 and tmp[y+1][x]!=k:
            stack.append([x,y+1])

n,m=map(int,input().split())
tmp=[]
for i in range(n):
    tmp.append([*map(int,input().split())])
ttmp=copy.deepcopy(tmp)
t=[]
res=0
for i in range(n):
    for j in range(m):
        if not tmp[i][j]:
            dfs(j,i,1)
            res+=1
t.append(res)

tmp=copy.deepcopy(ttmp)
res=0
for i in range(n):
    for j in range(m):
        if tmp[i][j]:
            dfs(j,i,0)
            res+=1
t.append(res)

print(*t)
