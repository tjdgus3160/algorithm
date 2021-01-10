# 2607번
import copy
import sys
input=sys.stdin.readline

key=""
klen=0
res=0
dic={}
for i in range(int(input())):
    s=input().rstrip('\n')
    if i ==0:
        key=s
        klen=len(s)
        for j in s:
            dic.setdefault(j,0)
            dic[j]+=1
        continue
    flag=True
    if len(s)==klen:
        tmp=copy.deepcopy(dic)
        k=1
        for j in s:
            if j in tmp and tmp[j]>0:
                tmp[j]-=1
            elif k>0:
                k-=1
            else:
                flag=False
                break
    elif len(s)+1==klen:
        tmp=copy.deepcopy(dic)
        for j in s:
            if j in tmp and tmp[j]>0:
                tmp[j]-=1
            else:
                flag=False
                break
    elif len(s)-1==klen:
        tmp=copy.deepcopy(dic)
        k=1
        for j in s:
            if j in tmp and tmp[j]>0:
                tmp[j]-=1
            elif k > 0:
                k -= 1
            else:
                flag=False
                break
    else:
        flag=False
    if flag:
        res+=1
print(res)