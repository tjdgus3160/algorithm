from collections import deque
import sys
input=sys.stdin.readline

v,n=map(int,input().split())
adj={}
degree=[0 for i in range(v+1)]
degree[0]=1
res=[]
for _ in range(n):
    a, b = map(int, input().split())
    adj.setdefault(a,[]).append(b)
    degree[b]+=1

if degree.count(0)==0:
    print(-1)
    exit()
dq=deque([degree.index(0)])
while dq:
    node=dq.popleft()
    res.append(node)
    if node in adj:
        tmp=[]
        for i in adj[node]:
            degree[i]-=1
            if degree[i]==0:
                k=i
                tmp.append(k)

        if len(tmp)>1:
            for i in tmp:
                k=i
                while True:
                    flag = True
                    if k in adj:
                        for j in adj[k]:
                            degree[j] -= 1
                            if degree[j] == 0:
                                tmp.append(j)
                                flag = False
                                k = j
                    if flag:
                        break
        tmp.sort()
        dq.extend(tmp)

if len(res)==v:
    for i in res:
        print(i)
else:
    print(-1)
