# hint itertools 순열 함수 사용
import itertools
def solution(numbers):
    answer = 0
    n=len(numbers)
    s=set()
    while n>0:
        s.update(set([int("".join(i)) for i in itertools.permutations(numbers,n)]))
        n-=1
    for i in list(s):
        if i >=2:
            p=1
            for j in range(2,i//2+1):
                if i%j==0:
                    p=0
                    break
            if p:
                answer+=1
    return answer

n='011'
print(solution(n))

# 집합에서 소수 판별
s -= set(range(0, 2))   # 0,1 제거
for i in range(2, int(max(s) ** 0.5) + 1):  # 최대수 제곱근+1까지
    s -= set(range(i * 2, max(s) + 1, i))   # i의 배수 집합에서 모두 제거