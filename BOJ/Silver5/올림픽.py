# 8979번
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
arr=[]
for _ in range(n):
    i,*a=map(int,input().split())
    arr.append(a)
    if i==k:
        t=a
res=1
for i in range(n):
    if arr[i][0]>t[0]:
        res+=1
    elif arr[i][0]==t[0]:
        if arr[i][1] > t[1]:
            res += 1
        elif arr[i][1]==t[1]:
            if arr[i][2] > t[2]:
                res += 1
print(res)