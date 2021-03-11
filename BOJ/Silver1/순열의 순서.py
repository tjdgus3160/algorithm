# 1722번
from math import factorial
import sys
input=sys.stdin.readline

n=int(input())
c,*arr=map(int,input().split())

fac=[factorial(i) for i in range(21)] # 팩토리얼 미리 저장
check=[False]*21    # 각 자리수 사용 유무

if c==1:
    k=arr[0] # k번째 순서 순열 구하
    res=[]
    for i in range(n): # 각 자리수
        for j in range(1,n+1): # 들어갈 숫자
            if check[j]: continue
            if k>fac[n-i-1]:
                k-=fac[n-i-1]
            else:
                res.append(j)
                check[j]=True
                break
    print(*res)
else:
    res=1
    for i in range(n): # 각 자리수
        for j in range(1,arr[i]): # 배치된 숫자의 순서
            if check[j]: continue
            res+=fac[n-i-1]
        check[arr[i]]=True
    print(res)
