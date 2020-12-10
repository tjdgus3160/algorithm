# 1516번
import sys
import queue
input=sys.stdin.readline
n=int(input())
time=[0]*(n+1)
degree=[0]*(n+1)
graph={}
prev=[[]]
result=[]
for i in range(1,n+1):
    time[i],*a=map(int,input().split())
    del a[-1]
    prev.append(a)
    for j in a:
        if j in graph:
            graph[j].append(i)
        else:
            graph[j]=[i]
        degree[i] += 1
q=queue.Queue()
for i in range(1,n+1):
    if degree[i]==0:
        q.put(i)
while not q.empty():
    tmp=q.get()
    result.append(tmp)
    if tmp not in graph:
        continue
    for i in graph[tmp]:
        degree[i]-=1
        if degree[i]==0:
            q.put(i)
for i in result:
    if prev[i]:
        max=0
        for j in prev[i]:
            if time[j]>max:
                max=time[j]
        time[i]+=max
for i in range(1,n+1):
    sys.stdout.writelines("{}\n".format(time[i]))