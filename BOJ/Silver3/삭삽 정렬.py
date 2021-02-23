# 13884번
import sys
input=sys.stdin.readline

for i in range(int(input())):
    k,n=map(int,input().split())
    arr=[]
    while len(arr)<n:
        tmp=[*map(int,input().split())]
        arr.extend(tmp)
    cur = float('inf')
    tmp=[]
    res=0
    for v in arr:
        while tmp and v<tmp[-1]:
            if tmp[-1]<cur:
                cur=tmp[-1]
            tmp.pop()
            res+=1
        if v>cur:
            res+=1
        else:
            tmp.append(v)
    print(k, res)
