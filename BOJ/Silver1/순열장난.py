# 10597번
import sys
input=sys.stdin.readline

def func(s,tmp,n):
    global res
    if not s:
        res=tmp[:]
        return
    if not res and int(s[0]) not in tmp and int(s[0])<=n:
        tmp.append(int(s[0]))
        func(s[1:],tmp,n)
        tmp.pop()
    if not res and len(s)>1 and int(s[:2]) not in tmp and int(s[:2])<=n:
        tmp.append(int(s[:2]))
        func(s[2:],tmp,n)
        tmp.pop()

s=input().rstrip()
m=len(s)
n=0
while m:
    n+=1
    if n<10:
        m-=1
    else:
        m-=2
res=[]
func(s,[],n)
print(*res)
