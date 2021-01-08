# 1764번
import sys
input=sys.stdin.readline

dic={}
n,m=map(int,input().split())
for _ in range(n):
    s=input().rstrip('\n')
    dic[s]=1
res=[]
cnt=0
for _ in range(m):
    s = input().rstrip('\n')
    if s in dic:
        res.append(s)
        cnt+=1
print(cnt)
for i in sorted(res):
    print(i)