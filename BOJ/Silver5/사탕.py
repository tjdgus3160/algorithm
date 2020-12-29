# 1812번
import sys
input=sys.stdin.readline

n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))
k=0
res=[0]*n
while True:
    for i in range(n):
        if i==0:
            res[i]=k
        else:
            res[i]=a[i-1]-res[i-1]
    if res[0]+res[-1]==a[-1]:
        break
    k+=1
for i in res:
    print(i)