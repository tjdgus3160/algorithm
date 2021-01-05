# 10814번
import sys
input=sys.stdin.readline

res=[]
for i in range(int(input())):
    age,name=input().split()
    res.append([i,int(age),name])
for i in sorted(res,key=lambda x:(x[1],x[0])):
    print(*i[1:])