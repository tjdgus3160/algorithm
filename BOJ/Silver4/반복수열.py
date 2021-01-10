# 2331번
import sys
input=sys.stdin.readline

arr=[]
*arr,p=map(int,input().split())
res=1
while True:
    k=sum([pow(int(i),p) for i in list(str(arr[-1]))])
    if k in arr:
        res=arr.index(k)
        break
    res+=1
    arr.append(k)
print(res)

