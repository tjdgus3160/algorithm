#재귀 O(2^n)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1)+fib(n-2)

print(fib(4))

#비재귀 O(n)
def fibo(n):
    if n<2:
        return n
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a

print(fibo(5))

# 수식사용 O(1) (단, 70번째 이상의 결과는 부정확)
import math
def fibos(n):
    sq5 = math.sqrt(5)
    phi = (1+sq5)/2
    return int(math.floor(phi**n/sq5))

# 제너레이터 사용, 전체 시퀀스를 한 번에 메모리에 생성하고 순회
def fibog():
    a,b=0,1
    while True:
        yield b
        a,b=b,a+b

fg=fibog()
for _ in range(10):
    print(next(fg), end=" ") # 출력: 1 1 2 3 5 8 13 21 34 55

# 동적 프로그래밍
def fiboDP(n, lookup):
    if n <=1:
        return n
    if lookup[n] is None:
        lookup[n]=fiboDP(n-2,lookup)+fiboDP(n-1,lookup)

    return lookup[n]

n=100
lookup=[None]*(n+1)
print(fiboDP(n,lookup))

