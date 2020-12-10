import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
res=[]
for i in range(n,m+1):
    if i==1:
        continue
    flag=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            flag=False
            break
    if flag:
        res.append(i)
print(sum(res))
print(min(res))
