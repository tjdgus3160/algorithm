# 1251번
import itertools
import sys
input=sys.stdin.readline

def find(s1,s2,s3):
    s1.reverse()
    s2.reverse()
    s3.reverse()
    s1="".join(s1)
    s2="".join(s2)
    s3="".join(s3)
    return "".join([s1,s2,s3])

n=list(input())
if n[-1]=='\n':
    del n[-1]
res=[]
for i in range(1,len(n)):
    for j in range(i+1,len(n)):
        s=find(n[0:i],n[i:j],n[j:])
        res.append(s)
res.sort()
print(res[0])