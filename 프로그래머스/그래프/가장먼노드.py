# 간선 표현시 2차원 배열에 0이 많으면 시간이 많이 소요됨으로 딕셔너리로 시간 단축

from collections import deque
def solution(n, edge):
    answer = 0
    v=[False]*(n+1)
    adj={}
    for i,j in edge:
        adj.setdefault(i,[]).append(j)
        adj.setdefault(j,[]).append(i)
    dq=deque([1])
    v[1]=True
    while dq:
        answer=k=len(dq)
        while k>0:
            t=dq.popleft()
            for i in adj[t]:
                if not v[i]:
                    dq.append(i)
                    v[i] = True
            k-=1
    return answer

n=6
arr=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,arr))
