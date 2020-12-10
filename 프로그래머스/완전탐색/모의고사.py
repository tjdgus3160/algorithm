# 3번 비교, 시간 차이 안남
def solution(arr):
    answer=[]
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    aa=len([i for i,j in zip(a*2000,arr) if i==j])
    bb=len([i for i,j in zip(b*1250,arr) if i==j])
    cc=len([i for i,j in zip(c*1000,arr) if i==j])
    t=max(aa,bb,cc)
    if aa==t:
        answer.append(1)
    if bb==t:
        answer.append(2)
    if cc == t:
        answer.append(3)
    return answer

arr=[1,2,3,4,5]
print(solution(arr))

# 한번 비교
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []
    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
    return result