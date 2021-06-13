# 5639번
from bisect import bisect
import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

def post(s,e):
    if s>e:
        return
    k=bisect(pre,pre[s],s+1,e)
    post(s+1,k)
    post(k,e)
    print(pre[s])

pre=[]
while True:
    try: pre.append(int(input()))
    except: break

post(0,len(pre))