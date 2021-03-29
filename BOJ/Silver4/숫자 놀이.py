# 2777번
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    arr=[]
    k=n
    while True:
        flag=True
        for i in range(2,int(k**0.5)+1):
            if k%i==0:
                arr.append(i)
                k=k//i
                flag=False
                break
        if flag:
            break
    if len(str(k))>1:
        print(-1)
        continue
    arr.append(k)
    res=0
    cur=0
    for i in arr:
        if cur==0:
            cur=i
        elif cur*i<10:
            cur*=i
        else:
            res+=1
            cur=i
    print(res+1)
