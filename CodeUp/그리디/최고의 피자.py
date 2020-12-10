import sys
input=sys.stdin.readline

n=int(input())
a,b=map(int,input().split())
c=int(input())

tmp=[]
for i in range(n):
    tmp.append(int(input()))
tmp.sort(reverse=True)
kal=c
cnt=a
res=kal//cnt
for i in tmp:
    if res<i//b:
        kal+=i
        cnt+=b
        res=kal//cnt
print(res)

