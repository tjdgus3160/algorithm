from itertools import product

def solution(n, s, a, b, fares):
    res=float('inf')
    graph=[[float('inf')]*(n+1) for _ in range(n+1)]
    for u,v,w in fares:
        graph[u][v]=w
        graph[v][u]=w
    for i in range(n+1):
        graph[i][i]=0

    for k, i, j in product(range(1, n + 1), repeat=3):
        if graph[i][j] > graph[i][k] + graph[k][j]:
            graph[i][j] = graph[i][k] + graph[k][j]

    for i in range(1,n+1):
        res=min(res,graph[s][i]+graph[i][a]+graph[i][b])
    return res

n=6
s=4
a=6
b=2
fares=[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n,s,a,b,fares))