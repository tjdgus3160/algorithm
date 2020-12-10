# 넓이 이용
def solution(brown, yellow):
    answer = []
    for i in range(1,(int((yellow+1)**0.5))+1):
        if yellow%i==0:
            t=(yellow//i+2)*(i+2)
            if t==brown+yellow:
                answer.append(yellow//i+2)
                answer.append(i+2)
                break
    return answer

print(solution(24,24))

# 둘레이용
# if 2*(i + yellow//i) == brown-4: