# 2644번
import sys
input=sys.stdin.readline

n=int(input())
a,b=map(int,input().split())
dic={}
for i in range(n):
    dic.setdefault(i,0)
for _ in range(int(input())):
    p,c=map(int,input().split())
    dic[c]=p
al=[a]
bl=[b]
while dic[a]:
    al.append(dic[a])
    a=dic[a]
while dic[b]:
    bl.append(dic[b])
    b=dic[b]
flag=True
for i in range(len(al)):
    for j in range(len(bl)):
        if al[i]==bl[j]:
            print(i+j)
            flag=False
            break
    else:
        continue
    break
if flag:
    print(-1)
