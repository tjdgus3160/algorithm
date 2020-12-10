# hint: 1000이하임으로 모든 문자열*3해서 자리수 맞쳐준뒤 정렬
def solution(numbers):
    n = sorted(map(str, numbers), key=lambda x:x*3, reverse=True)
    return str(int("".join(n)))

n=[3,30,34,5,9]
print(solution(sorted(n)))
