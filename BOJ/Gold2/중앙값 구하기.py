# 2696번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    k=0
    arr=[]
    res=[]
    while k<n:
        s=[*map(int,input().split())]
        for i in s:
            arr.append(i)
            if k%2==0:
                arr.sort()
                res.append(arr[len(arr)//2])
            k+=1
    print(len(res))
    if len(res)>10:
        for i in range(len(res)//10+1):
            print(*res[i*10:i*10+10])
    else:
        print(*res)
