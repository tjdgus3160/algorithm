dx=[1,-1,-1,1]
dy=[1,1,-1,-1]

def check(x,y,k):
    if k==0:
        return arr[y][x]
    gold=0
    y-=k
    for i in range(4):
        for _ in range(k):
            x=x+dx[i]
            y=y+dy[i]
            if 0<=x<n and 0<=y<n:
                gold+=arr[y][x]
    return gold

n,m=map(int,input().split())
arr=[[*map(int,input().split())] for _ in range(n)]
res=0
for y in range(n):
    for x in range(n):
        gold=0
        for k in range(2*(n-1)+1):
            gold+=check(x,y,k)
            if gold*m >= pow(k,2)+pow(k+1,2):
                res=max(res,gold)
print(res)