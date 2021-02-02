# 10546번
import sys
input=sys.stdin.readline

n=int(input())
dic={}
for _ in range(n):
    s=input().rstrip('\n')
    dic.setdefault(s,0)
    dic[s]+=1
for _ in range(n-1):
    s=input().rstrip('\n')
    dic[s]-=1
res=''
for s,v in dic.items():
    if v==1:
        res=s
        break
print(res)