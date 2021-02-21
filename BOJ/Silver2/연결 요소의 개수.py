# 11724번
import sys
input=sys.stdin.readline

def find(x):
    if parent[x]==x:
        return x
    parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a,b=find(a),find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n,m=map(int,input().split())
parent=[*range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    union(u,v)
res=0
for i in range(1,n+1):
    if parent[i]==i:
        res+=1
print(res)
