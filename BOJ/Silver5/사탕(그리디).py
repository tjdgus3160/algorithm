# 11256번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    j,n=map(int,input().split())
    arr=[]
    for _ in range(n):
        a,b=map(int,input().split())
        arr.append(a*b)
    res=0
    for i in sorted(arr,reverse=True):
        j-=i
        res+=1
        if j<=0:
            break
    print(res)