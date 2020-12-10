def solution(clothes):
    answer = 1
    d={}
    for i in clothes:
        d.setdefault(i[1],0)
        d[i[1]]+=1
    for i in list(d.values()):
        answer = answer * (i + 1)
    return answer-1
'''
# Counter 사용, 살짝 느림
from collections import Counter
def solution(clothes):
    answer = 1
    cnt=Counter([k for v,k in clothes])
    for i in list(cnt.values()):
        answer=answer*(i+1)
    return answer-1
'''
arr=[['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
print(solution(arr))