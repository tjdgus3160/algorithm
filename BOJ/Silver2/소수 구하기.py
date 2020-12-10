# 1929번
import sys

n,m=map(int,input().split())
prim=[True for _ in range(m+1)]
prim[1]=False
for i in range(2,int(m**0.5)+1):
    if prim[i]:
        j=i+i
        while j <=m:
            prim[j]=False
            j+=i
for i in range(n,m+1):
    if prim[i]:
        sys.stdout.writelines("{}\n".format(i))