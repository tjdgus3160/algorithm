from itertools import combinations
from collections import defaultdict
import sys
input=sys.stdin.readline

def check(tmp):
    res=[]
    for i in range(1,n+1):
        k=i
        for j in range(1,16):
            k=tmp[k][j]
        res.append(k)
    return res

def makedic(sub):
    tmp=defaultdict(dict)
    for i in range(1, n + 1):
        for j in range(1, 16):
            tmp[i][j] = i
    for a,b in sub:
        tmp[a][b]=a+1
        tmp[a+1][b]=a
    return tmp

n,m=map(int,input().split())
arr=[[*map(int,input().split())]for _ in range(m)]
dic=makedic(arr)
init=check(dic)
for i in range(len(arr)+1):
    for sub in combinations(arr,i):
        tmp=makedic(sub)
        if check(tmp)==init:
            print(len(sub))
            exit()