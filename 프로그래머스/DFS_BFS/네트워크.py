# 그룹 개수 구하기 dfs로 방문노드 체크
def solution(n, arr):
    answer = 0
    v=[False]*n
    l=[]
    for i in range(n):
        if not v[i]:
            l.append(i)
            while l:
                t=l.pop()
                v[t] = True
                for j,k in enumerate(arr[t]):
                    if not v[j] and k:
                        l.append(j)
            answer+=1
    return answer

arr=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n=3
print(solution(n,arr))