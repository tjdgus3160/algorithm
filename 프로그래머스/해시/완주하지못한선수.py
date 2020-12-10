def solution(participant, completion):
    answer = ""
    completion.sort()
    participant.sort()
    for i in range(len(completion)):
        if participant[i]!=completion[i]:
            answer=participant[i]
            break
    if answer=="":
        answer=participant[-1]
    return answer

# Counter 객체 사용
from collections import Counter
def solution(p, c):
    return list((Counter(p)-Counter(c)).keys())[0]

p=['leo', 'kiki', 'eden']
c=['eden', 'kiki']
print(Counter(p))
print(Counter(c))
print(Counter(p)-Counter(c))
print(solution(p,c))
