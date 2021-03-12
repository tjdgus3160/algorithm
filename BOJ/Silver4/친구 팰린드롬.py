# 15270번
import sys
input=sys.stdin.readline

def func(k,cnt):
    global res
    if k==m:
        if True in p:
            res=max(res,cnt+1)
        else:
            res=max(res,cnt)
        return
    if p[dic[k][0]] and p[dic[k][1]]:
        p[dic[k][0]]=False
        p[dic[k][1]]=False
        func(k+1,cnt+2)
        p[dic[k][0]] = True
        p[dic[k][1]] = True
    func(k+1,cnt)

n,m=map(int,input().split())
p=[True]*(n+1)
p[0]=False
if m==0:
    print(1)
    exit()
dic=[]
for _ in range(m):
    dic.append([*map(int,input().split())])
res=0
func(0,0)
print(res)