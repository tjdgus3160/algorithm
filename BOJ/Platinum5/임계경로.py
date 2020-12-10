# 1948번
import queue
import sys
input=sys.stdin.readline

n=int(input())
degree=[0]*(n+1)    # 진입 차수 저장
time=[0]*(n+1)      # 임계 경로 저장
graph={}
back={}
for _ in range(int(input())):
    u,v,w=map(int,input().split())
    if u not in graph:
        graph[u]={v:w}
    else:
        graph[u][v]=w
    if v not in back:
        back[v]={u:w}
    else:
        back[v][u]=w
    degree[v]+=1
start,end=map(int,input().split())
q=queue.Queue()
for i in range(1,n+1):
    if degree[i]==0:
        q.put(i)
while not q.empty():
    tmp=q.get()
    if tmp not in graph:
        continue
    for i in graph[tmp].keys():
        degree[i]-=1
        time[i]=max(time[i],graph[tmp][i]+time[tmp])
        if degree[i]==0:
            q.put(i)
q.put(end)
cnt=[]
v=[]
cnt=0
while not q.empty():
    tmp=q.get()
    v.append(tmp)
    if tmp==start:
        break
    for i in back[tmp].keys():
        if time[tmp]-back[tmp][i]==time[i]:
            cnt+=1
            if i not in v:
                q.put(i)
                v.append(i)
print(time[end])
print(cnt)