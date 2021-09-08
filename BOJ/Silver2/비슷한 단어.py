# 1411번
from itertools import combinations
import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    s=input().rstrip()
    dic={}
    k=0
    tmp=''
    for i in s:
        if i not in dic:
            dic[i]=k
            k+=1
        tmp+=str(dic[i])
    arr.append(tmp)
res=0
for a,b in combinations(arr,2):
    if a==b:
        res+=1
print(res)