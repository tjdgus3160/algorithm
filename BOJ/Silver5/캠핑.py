# 4796번
import sys
input=sys.stdin.readline

k=1
while True:
    l,p,v=map(int,input().split())
    if l==0 and p==0 and v==0:
        break

    print("Case %d: %d"%(k,l*(v//p)+min(l,v%p)))
    k+=1