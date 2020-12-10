def SuperSum(k, n, Kcount, Ncount, A) :
    # 위쪽 값과 우측 값 더한 후 삽입
    A[Kcount][Ncount] = (A[Kcount-1][Ncount] + A[Kcount][Ncount-1])

    # 배열은 index가 0 부터 / 재귀 탈출 부분
    if Kcount == k-1 and Ncount == n-1 :
        print(A[k-1][n-1])
        return
    if Ncount == n-1 :
        Ncount = 1
        SuperSum(k, n, Kcount+1, Ncount, A)
    else :
        SuperSum(k, n, Kcount, Ncount+1, A)

if __name__ == '__main__' :
    while True :
        try :
            k, n = map(int, input().split())

            # 배열 선언
            A = [[i for i in range(1, n+1)] for _ in range(k)]
            # K가 1 일 경우
            if k == 1 :
                sum = 0
                for i in range(n) :
                    sum += A[k-1][i]
                print(sum)
                continue
            # N 이 1 일 경우
            elif n == 1:
                print(1)
                continue
            SuperSum(k, n, 0, 1, A)
        except EOFError :
            # EOF Error 예외 처리
            break
