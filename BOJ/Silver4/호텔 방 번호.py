# 5671번
import sys
input=sys.stdin.readline

def func(n,m):
    res=0
    for i in range(n,m+1):
        for j in str(i):
            if str(i).count(j)>1:
                break
        else:
            res+=1
    return res

while True:
    try:
        n,m=map(int,input().split())
        print(func(n,m))
    except:
        break