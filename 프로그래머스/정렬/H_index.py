# 순차 탐색 느림
def solution(arr):
    answer = 1
    arr.sort()
    while True:
        t=len([i for i in arr if i>=answer])
        if answer<=t:
            if len(arr)==t+len([i for i in arr if i<answer]):
                answer+=1
                continue
        break
    return answer-1
c=[0,1,2,5,6]
print(solution(c))

# hint: 요소로 탐색 빠름, l-i로 이상인 논문 수 쉽게 구함
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0