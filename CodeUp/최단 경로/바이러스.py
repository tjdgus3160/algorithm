import sys
input=sys.stdin.readline

n=int(input())
adj=[[0 for _ in range(n+1)] for _ in range(n+1)]
tmp=[]
for i in range(int(input())):
    a,b=map(int,input().split())
    adj[a][b]=1
    adj[b][a]=1

stack=[1]
v=[1]
while stack:
    node=stack.pop()
    for i in range(1,n+1):
        if adj[node][i] and i not in v:
            stack.append(i)
            v.append(i)

print(len(v)-1)

