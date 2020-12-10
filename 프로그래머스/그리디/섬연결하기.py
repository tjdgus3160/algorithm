# hint: 크루스칼 알고리즘 적은 비용으로 모든 노드 연결, union-find사용
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    parent=[i for i in range(n)]
    for u,v,w in costs:
        if parent[u] != parent[v]:
            t=parent[v]
            for i in range(n):
                if parent[i]==t:
                    parent[i] = parent[u]
            answer+=w
        if sum(parent)==0:
            break
    return answer

c=[[0,2,1],[1,3,1],[0,1,2],[1,2,8]]
n=4
print(solution(n,c))