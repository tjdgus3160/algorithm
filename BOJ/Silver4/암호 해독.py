# 2149번
import copy
import sys
input=sys.stdin.readline

key=list(input().rstrip('\n'))
s=input().rstrip('\n')
k=copy.deepcopy(key)
key.sort()
arr=[]
cnt=len(s)//len(key)
for i in range(len(key)):
    arr.append(list(s[i*cnt:i*cnt+cnt]))
a=[]
for i in k:
    t=key.index(i)
    a+=[arr.pop(t)]
    key.remove(i)
res=""
for _ in range(cnt):
    for i in range(len(a)):
        res+=a[i].pop(0)
print(res)