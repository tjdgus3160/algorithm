# 3048번
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
d={}
s1=input().rstrip()
for i in s1:
    d[i]='R'
s2=input().rstrip()
for i in s2:
    d[i]='L'
t=int(input())
res=list(s1[::-1])+list(s2)
for _ in range(t):
    tmp=[]
    for i in range(len(res)-1):
        if d[res[i]]=='R' and d[res[i+1]]=='L' and i-1 not in tmp:
            tmp.append(i)
    for i in tmp:
        res[i],res[i+1]=res[i+1],res[i]
print(''.join(res))