# 4375번
import sys
input=sys.stdin.readline

def func(n):
    if n==1:
        return 1
    k=int('1'*(len(str(n))+1))
    cnt=len(str(k))
    while True:
        if k%n==0:
            return cnt
        k+=10**cnt
        cnt+=1

while True:
    try:
        n=int(input())
        print(func(n))
    except:
        break
