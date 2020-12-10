import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

def find(a,b):
    if a > b:
        a, b = b, a
    global res
    if a==b:
        return
    if a%2==0 and a==b-1:
        res+=2
        return
    if b-a>2:
        res += 1
        return find(a,b//2)
    else:
        if a==1:
            res+=1
            return find(a,b//2)
        else:
            res+=2
            return find(a//2,b//2)


a,b=map(int,input().split())
if a>b:
    a,b=b,a
res=0
find(a,b)
print(res)

