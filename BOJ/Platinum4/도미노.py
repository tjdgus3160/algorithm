# 4196번
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x):
    global idd,scc
    id[x]=idd=idd+1
    l.append(x)
    parent=id[x]
    for i in a[x]:
        if id[i]==0:
            parent=min(parent,dfs(i))
        if not finish[i]:
            parent=min(parent,id[i])
    if parent==id[x]:
        tmp=[]
        while True:
            t=l.pop()
            tmp.append(t)
            group[t]=len(scc)+1
            finish[t]=True
            if x==t:
                break
        scc.append(tmp)
    return parent

c=int(input())
for _ in range(c):
    n,e=map(int,input().split())
    idd=0
    id=[0]*(n+1)
    finish=[False]*(n+1)
    scc=[]
    l=[]
    indegree=[False]*(n+1)
    group=[0]*(n+1)
    a=[[] for _ in range(n+1)]
    for _ in range(e):
        v,u=map(int,input().split())
        a[v]+=[u]
    for i in range(1,n+1):
        if id[i]==0:
            dfs(i)
    for i in range(1,n+1):
        for j in a[i]:
            if group[i]!=group[j]:
                indegree[group[j]]=True
    print(indegree[1:len(scc)+1].count(False))