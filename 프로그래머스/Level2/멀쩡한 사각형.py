from math import gcd

def solution(w,h):
    # 점을 지날때 1개 사용
    # 선을 지날때 2개 사용
    # w*h-(h*2-점의 수(=gcd)*2)
    # 다시 정리하면 아래와 같은
    return w*h-(w+h-gcd(w,h))식

print(solution(2,2))