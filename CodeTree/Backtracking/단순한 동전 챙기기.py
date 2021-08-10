from itertools import permutations
import sys
input=sys.stdin.readline

def func(tmp):
    res=0
    res+=abs(dic[tmp[0]][0]-s[0])+abs(dic[tmp[0]][1]-s[1])
    res+=abs(dic[tmp[1]][0]-dic[tmp[0]][0])+abs(dic[tmp[1]][1]-dic[tmp[0]][1])
    res+=abs(dic[tmp[2]][0]-dic[tmp[1]][0])+abs(dic[tmp[2]][1]-dic[tmp[1]][1])
    res+=abs(dic[tmp[2]][0]-e[0])+abs(dic[tmp[2]][1]-e[1])
    return res

n=int(input())
s=[]
e=[]
dic={}
for y in range(n):
    tmp=input().rstrip()
    for x in range(n):
        if tmp[x]=='S':
            s=[x,y]
        elif tmp[x]=='E':
            e=[x,y]
        elif tmp[x]!='.':
            dic[int(tmp[x])]=[x,y]
m=len(dic)
if m<3:
    print(-1)
    exit()
res=float('inf')
for sub in permutations(dic.keys(),3):
    if sub[0]<sub[1] and sub[1]<sub[2]:
        res=min(res,func(sub))
print(res)