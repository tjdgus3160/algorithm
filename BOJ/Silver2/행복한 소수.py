# 10434번
import sys
input=sys.stdin.readline

n=10001
l=[True for _ in range(n+1)]
l[1]=False
for i in range(2,int(n**0.5)+1):
    if l[i]:
        j=i+i
        while j<=n:
            l[j]=False
            j+=i

memo=[False]*10001
for i in [1,10,130,97,49,7]:
    memo[i]=True

for _ in range(int(input())):
    idx,v=map(int,input().split())
    tmp=[v]
    value=v
    while True:
        k=0
        for i in list(str(value)):
            k+=int(i)*int(i)
        if k in tmp:
            print(idx,v,'NO')
            break
        if memo[k] or k==1:
            for s in tmp:
                memo[s]=True
            if l[v]:
                print(idx,v,'YES')
            else:
                print(idx, v, 'NO')
            break
        tmp.append(k)
        value=k