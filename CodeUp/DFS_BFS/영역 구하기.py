import sys
input=sys.stdin.readline

def dfs(a,b):
    stack=[[b,a]]
    v=[[b,a]]
    while stack:
        x,y=stack.pop()
        l[y][x]=1
        if x>0 and l[y][x-1]==0 and [x-1,y] not in v:
            stack.append([x-1,y])
            v.append([x-1, y])
        if x<m-1 and l[y][x+1]==0 and [x+1,y] not in v:
            stack.append([x+1,y])
            v.append([x+1, y])
        if y>0 and l[y-1][x]==0 and [x,y-1] not in v:
            stack.append([x,y-1])
            v.append([x, y-1])
        if y<n-1 and l[y+1][x]==0 and [x,y+1] not in v:
            stack.append([x,y+1])
            v.append([x, y+1])
    return len(v)

n,m,k=map(int,input().split())
l=[[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(n-y2,n-y1):
        for j in range(x1,x2):
            l[i][j]=1

cnt=0
res=[]
for i in range(n):
    for j in range(m):
        if l[i][j]==0:
            t=dfs(i,j)
            res.append(t)
            cnt+=1
res.sort()
print(cnt)
print(*res)
