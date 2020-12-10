# 2150번
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x):
    global idd,l,scc
    idd+=1
    id[x]=idd
    l+=[x]

    parent=id[x]
    for i in a[x]:
        if id[i]==0:
            parent=min(parent,dfs(i))
        if not finished[i]:
            parent=min(parent,id[i])
    if parent==id[x]:
        tmp=[]
        while True:
            t=l.pop()
            tmp.append(t)
            finished[t]=True
            if t==x:
                break
        scc+=[[*sorted(tmp)]]
    return parent

n,e=map(int,input().split())
a=[[] for _ in range(n+1)]
for _ in range(e):
    v,u=map(int,input().split())
    a[v].append(u)

idd=0
id=[0 for _ in range(n+1)]
finished=[False for _ in range(n+1)]
l=[]
scc=[]
for i in range(1,n+1):
    if id[i]==0:
        dfs(i)

print(len(scc))
for i in sorted(scc):
    for j in i:
        print(j,end=" ")
    print(-1)