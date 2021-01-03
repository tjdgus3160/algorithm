# 5800번
import sys
input=sys.stdin.readline

res=[]
for _ in range(int(input())):
    n,*tmp=map(int,input().split())
    tmp.sort()
    k=0
    for i in range(n-1):
       k=max(k,tmp[i+1]-tmp[i])
    res.append([tmp[-1],tmp[0],k])

for idx,sub in enumerate(res):
    print("Class",idx+1)
    print("Max %d, Min %d, Largest gap %d"%(sub[0],sub[1],sub[2]))