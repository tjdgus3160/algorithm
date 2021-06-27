# 11558번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    arr=[0]*(n+1)
    selected=[False]*(n+1)
    for i in range(1,n+1):
        arr[i]=int(input())
    selected[1]=True
    k=0
    cur=1
    while True:
        if cur==n:
            print(k)
            break
        cur=arr[cur]
        if selected[cur]:
            print(0)
            break
        selected[cur]=True
        k+=1

