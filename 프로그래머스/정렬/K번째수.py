def solution(array, commands):
    answer = []
    for a,b,c in commands:
        answer.append(sorted(array[a-1:b])[c-1])
    return answer

arr=[1, 5, 2, 6, 3, 7, 4]
c=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(arr,c))