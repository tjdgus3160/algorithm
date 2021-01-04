# 2621번
import sys
input=sys.stdin.readline

arr=[]
color={}
num={}
cnt=[]
res=0

def check(arr):
    arr.sort()
    k=arr[1]-arr[0]
    for i in range(1,5):
        if arr[i]-arr[i-1]!=k:
            return False
    return True

for _ in range(5):
    c,n=input().split()
    color.setdefault(c,[])
    color[c].append(int(n))
    num.setdefault(int(n),0)
    num[int(n)]+=1
    cnt.append(int(n))
    arr.append([c,int(n)])
if len(color)==1:
    if check(cnt):
        res=max(res,900+max(cnt))
    else:
        res=max(res,600+max(cnt))
elif 4 in num.values():
    tmp=0
    for k,v in num.items():
        if v==4:
            tmp=k
            break
    res=max(res,800+tmp)
elif 3 in num.values() and 2 in num.values():
    tmp=0
    for k,v in num.items():
        if v==3:
            tmp+=10*k
        else:
            tmp+=k
    res=max(res,700+tmp)
elif check(cnt):
    res=max(res,500+max(cnt))
elif 3 in num.values():
    tmp = 0
    for k, v in num.items():
        if v == 3:
            tmp = k
            break
    res = max(res, 400 + tmp)
elif list(num.values()).count(2)==2:
    tmp=[]
    for k, v in num.items():
        if v == 2:
            tmp.append(k)
    res = max(res, 300 + max(tmp)*10+min(tmp))
elif len(num)==4:
    tmp = 0
    for k, v in num.items():
        if v == 2:
            tmp = k
            break
    res = max(res, 200 + tmp)
else:
    res=max(res,100+max(cnt))
print(res)