import sys
input=sys.stdin.readline

def dfs(x,y,k):
    if tmp[x][y]==k:
        v[x][y]=1
        cnt=1
        stack=[[x,y]]
        while stack:
            x,y=stack.pop()
            if x>0 and tmp[x-1][y]==k and not v[x-1][y]:
                stack.append([x-1,y])
                v[x-1][y]=1
                cnt+=1
            if x<6 and tmp[x+1][y]==k and not v[x+1][y]:
                stack.append([x+1,y])
                v[x+1][y]=1
                cnt+=1
            if y>0 and tmp[x][y-1]==k and not v[x][y-1]:
                stack.append([x,y-1])
                v[x][y-1]=1
                cnt+=1
            if y<6 and tmp[x][y+1]==k and not v[x][y+1]:
                stack.append([x,y+1])
                v[x][y+1]=1
                cnt+=1
        if cnt>=3:
            return True
    return False


v=[[0 for _ in range(7)] for _ in range(7)]
tmp=[]
for i in range(7):
    tmp.append([*map(int,input().split())])

res=0
for i in range(7):
    for j in range(7):
        if not v[i][j]:
            if dfs(i,j,tmp[i][j]):
                res+=1
print(res)
