import itertools
import sys
input=sys.stdin.readline

res=[]
n=int(input())
for i in range(1,n-1):
    for j in range(1,n-i-1):
        tmp=[i,j,n-i-j]
        tmp.sort()
        s="".join(map(str,tmp))
        if s not in res and tmp[-1]<tmp[0]+tmp[1]:
            res.append(s)
print(len(res))
