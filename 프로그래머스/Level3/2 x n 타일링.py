def solution(n):
    a=2
    b=3
    if n<4:
        return n
    for i in range(4,n+1):
        a,b=b,a+b
    return b%1000000007