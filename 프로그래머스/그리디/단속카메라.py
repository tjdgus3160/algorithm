# hint: 끝기준 정렬하여 첫번째꺼부터 비교해나감
def solution(arr):
    arr.sort(key=lambda x:x[1])
    answer = 0
    tmp=-30000
    for i in arr:
        if tmp<i[0]:
            answer+=1
            tmp=i[1]
    return answer

arr=[[-20,15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(arr))