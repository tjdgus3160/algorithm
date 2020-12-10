# hint 이중 for문 일때는 빠져 나가는 조건 잘하면 시간 단축
def solution(phone_book):
    answer = True
    n=len(phone_book)
    phone_book.sort()
    for i in range(n):
        for j in range(i+1,n):
            if phone_book[i]==phone_book[j][:len(phone_book[i])]:
                answer=False
                break
        if not answer:
            break
    return answer

p=['12','123','1235','567','88']
print(solution(p))

# zip, startswith사용, 접미사라서 문자열에 대해 정렬 해도됌
# 다음원소와 짝 짓기 => zip(arr,arr[1:])
def solution(phone_book):
    answer = True
    phone_book.sort()
    for p1,p2 in zip(phone_book,phone_book[1:]):
        if p2.startswith(p1):
            answer=False
            break
    return answer