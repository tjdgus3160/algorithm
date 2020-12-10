# 3977번
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x):
    global cnt,sccC
    cnt+=1
    id[x]=cnt
    stack.append(x)
    parent=id[x]
    for i in a[x]:
        if id[i]==0:
            parent=min(parent,dfs(i))
        if sccn[i]==-1:
            parent=min(parent,id[i])
    if parent==id[x]:
        while stack:
            t=stack.pop()
            sccn[t]=sccC
            if x==t:
                break
        sccC+=1
    return parent

for _ in range(int(input())):
    n,e=map(int,input().split())
    a = [[] for _ in range(n)]  # 간선 저장
    id=[0]*(n)                  # scc 과정 정점 id
    sccn = [-1] * (n)           # scc 번호 할당(완료 여부, 그룹 id 동시 확인 가능)
    stack=[]                    # 스택
    sccC=cnt=0

    for _ in range(e):  # 간선 정보 저장
        v,u=map(int,input().split())
        a[v].append(u)
    for i in range(n):  # scc 수행
        if id[i]==0:
            dfs(i)
    degree = [False] * sccC  # 진입차수
    for i in range(n):  # 모든 간선을 확인하여 그룹별 진입차수 확인
        for j in a[i]:
            if sccn[i]!=sccn[j]: # i,j(i->j) 의 그룹id가 다르면 j그룹은 진입차수 존재
                degree[sccn[j]]=True
    result=[]
    for i in range(sccC):
        if not degree[i]:
            result.append(i)
    if len(result)==1:
        for u in range(n):
            if sccn[u]==result[0]:
                print(u)
    else:
        print('Confused')
    input()
    print()