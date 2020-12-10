# hint: 레벨1부터 n까지 전체 사람 수 total에서 빼가면서 진행
def solution(n, arr):
    answer = []
    total=len(arr)
    for i in range(1,n+1):
        if total:
            cnt=arr.count(i)
            answer.append([cnt/total,i])
            total-=cnt
        else:
            answer.append([0,i])
    return [i[1] for i in sorted(answer,key=lambda x:(-x[0],x[1]))]

n=5
arr=[2, 1, 2, 6, 2, 4, 3, 3]
print(solution(n,arr))