# 정렬해서 앞뒤로 하나씩 빼기
from collections import deque
def solution(arr, w):
    answer = 0
    dq=deque(sorted(arr))
    while dq:
        if dq[0]+dq[-1]<=w:
            dq.popleft()
            if dq:
                dq.pop()
            answer+=1
        else:
            dq.pop()
            answer+=1
    return answer


p=[50,50,60,70,80,20, 20, 20]
w=100
print(solution(p,w))

# 인덱스 사용, 2명씩 같이 탄 사람 수=answer
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit:
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer