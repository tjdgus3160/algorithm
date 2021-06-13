# 1389번
import sys
input=sys.stdin.readline

def func(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if i!=j and i!=k and j!=k:
                    dist[j][k]=min(dist[j][k],dist[j][i]+dist[i][k])
    s=float('inf')
    for i in dist:
        s=min(s,sum(i[1:]))
    return [i for i in range(1,n+1) if sum(dist[i][1:])==s][0]

n,m=map(int,input().split())
dist=[[float('inf')]*(n+1) for i in range(n+1)]
for i in range(1,n+1):
    dist[i][i]=0
for _ in range(m):
    a,b=map(int,input().split())
    dist[a][b]=1
    dist[b][a]=1

print(func(n))