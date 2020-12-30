# 2238번
import sys
input=sys.stdin.readline

u,n=map(int,input().split())
cnt={}
dict={}
for i in range(n):
    s,p=input().split()
    cnt.setdefault(int(p),0)
    cnt[int(p)]+=1
    dict.setdefault(int(p),[])
    dict[int(p)].append(s)
arr=sorted(cnt.items(),key=lambda x:(x[1],x[0]))
price=arr[0][0]
name=dict[price][0]
print(name,price)