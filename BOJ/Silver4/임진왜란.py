# 3077번
import sys
input=sys.stdin.readline

n=int(input())
total=n*(n-1)//2
ans=input().split()
dic={}
for idx,v in enumerate(ans):
    dic[v]=idx
arr=input().split()
res=0
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if dic[arr[i]]<dic[arr[j]]:
            res+=1
print(str(res)+'/'+str(total))