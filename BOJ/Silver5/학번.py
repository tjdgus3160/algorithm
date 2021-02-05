# 3711번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    arr=[]
    for _ in range(n):
        arr.append(int(input()))
    k=1
    while True:
        tmp=[i%k for i in arr]
        if len(set(tmp))==n:
            break
        k+=1
    print(k)