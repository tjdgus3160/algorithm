# 1339번
from collections import defaultdict
import sys
input=sys.stdin.readline

n=int(input())
dic=defaultdict(list)
arr=[]
for _ in range(n):
    s=input().rstrip()
    arr.append(s)
    for i in range(len(s)):
        dic[s[i]].append(pow(10,len(s)-i-1))

d={}
for idx,v in enumerate(sorted(dic.items(),key=lambda x:(-sum(x[1])))):
    d[v[0]]=9-idx
res=0
for word in arr:
    tmp=''
    for i in word:
        tmp+=str(d[i])
    res+=int(tmp)

print(res)