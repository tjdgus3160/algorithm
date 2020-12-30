# 2089번
import sys
input=sys.stdin.readline

def func(n):
    if n==0:
        res.append(0)
        return
    if n==1:
        res.append(1)
        res.reverse()
        return
    if n<0:
        if -n%2==0:
            res.append(0)
        else:
            res.append(1)
        func((-n+1)//2)
    else:
        res.append(n%2)
        func(-(n//2))
n=int(input())
res=[]
func(n)
print("".join(map(str,res)))