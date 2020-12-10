# hint: 이미 들어온 수 중 진입한 수보다 작으면 k번까지 삭제
def solution(n, k):
    stack =[]
    for i in n:
        while stack and stack[-1]<i and k>0:
            stack.pop()
            k-=1
        stack.append(i)
    return "".join(stack[:len(n)-k])

n="4177252841"
k=4
print(solution(n,k))
