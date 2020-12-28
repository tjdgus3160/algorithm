# 1676번
import sys
input=sys.stdin.readline

def func(n):
    if n == 0:
        return 0
    num = 1
    res = 0
    for i in range(2, n + 1):
        num *= i
        num %= 1000000
        while num % 10 == 0:
            res+=1
            num//=10
    return res

n=int(input())
print(func(n))